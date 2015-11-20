# coding: utf-8
import numpy as np
import cv2
import inspect

# top left, top right, bottom right, bottom left
POINTS_ORDER = ((0, 0), (1, 0), (1, 1), (0, 1))


def order_points(points):
    return _order_points_angle(points)


def ordered(*arg_names):
    def decorator(func):
        argspec = inspect.getargspec(func)
        def wrapper(*args, **kwargs):
            for arg in arg_names:
                index = argspec.args.index(arg)
                if index < len(args):
                    ordered_points = order_points(args[index])
                    try:
                        args[index] = ordered_points
                    except TypeError:
                        args = list(args)
                        args[index] = ordered_points
                elif arg in kwargs.keys():
                    kwargs[arg] = order_points(kwargs[arg])
            return func(*args, **kwargs)
        return wrapper
    return decorator


def _order_points_sum_diff(points):
    """Orders a list of four points so that the result list is top left, top
    right, bottom right, bottom left"""
    ordered_points = [None for _ in range(4)]
    sorted_by_sum = sorted(points, key=lambda x: x[0] + x[1])
    sorted_by_diff = sorted(points, key=lambda x: x[0] - x[1])
    ordered_points[0] = sorted_by_sum[0]
    ordered_points[1] = sorted_by_diff[-1]
    ordered_points[2] = sorted_by_sum[-1]
    ordered_points[3] = sorted_by_diff[0]
    return ordered_points


def _order_points_angle(points):
    """Orders a list of four points so that the result list is top left, top
    right, bottom right, bottom left"""
    ordered_points = [None for _ in range(4)]
    sorted_by_sum = sorted(points, key=lambda x: x[0] + x[1])
    ordered_points[0] = sorted_by_sum[0]
    sorted_by_sum.remove(ordered_points[0])
    sorted_by_angle = sorted(sorted_by_sum,
                             key=lambda x: _get_angle(ordered_points[0], x),
                             reverse=True)
    ordered_points[1:] = sorted_by_angle
    return ordered_points


def _get_angle(p1, p2):
    return np.arctan2((p2[0] - p1[0]), (p2[1] - p1[1]))


def distance(point_a, point_b):
    """Returns the distance between point_a and point_b in 2D space"""
    x_diff = point_a[0] - point_b[0]
    y_diff = point_a[1] - point_b[1]
    return np.sqrt(x_diff ** 2 + y_diff ** 2)


@ordered('points')
def get_target_rectangle_size(points):
    """Returns the max (width, height) of a quadrilateral"""
    top_width = distance(points[0], points[1])
    bottom_width = distance(points[2], points[3])
    width = max(int(top_width), int(bottom_width))

    left_height = distance(points[0], points[3])
    right_height = distance(points[1], points[2])
    height = max(int(left_height), int(right_height))
    return width, height


@ordered('points')
def process(image, points):
    width, height = get_target_rectangle_size(points)
    expected_points = [(el[0] * width, el[1] * height) for el in POINTS_ORDER]

    # get the transform matrice and apply it to the image
    np_points = [np.array(p, dtype='float32')
                 for p in (points, expected_points)]
    matrice = cv2.getPerspectiveTransform(*np_points)
    return cv2.warpPerspective(image, matrice, (width, height))


def resize(image, ratio=None, height=None, width=None):
    image_height, image_width = image.shape[:2]
    if height and width:
        pass
    elif height:
        ratio = height / image_height
    elif width:
        ratio = width / image_width
    if ratio:
        height, width = (int(el * ratio) for el in image.shape[:2])
    if height is None or width is None:
        raise ValueError("at least one of ratio, height or width must be provided")

    return cv2.resize(image, (width, height))


def detect_englobing_polygon(image, edge_count=4):
    resized_image = resize(image, width=500)
    ratio = image.shape[0] / resized_image.shape[0]
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), .4)
    edge = cv2.Canny(blur, 250, 750)

    _, contours, _ = cv2.findContours(edge.copy(),
                                      cv2.RETR_LIST,
                                      cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        if len(approx) == edge_count:
            result = approx
            break
    else:
        raise LookupError("No polygon deteted")
    return result * ratio
