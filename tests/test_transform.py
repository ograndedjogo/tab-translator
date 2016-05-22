import numpy as np
import cv2
from tabtranslator.transform import ordered, order_points, distance, \
                                    get_target_rectangle_size, resize, \
                                    detect_englobing_polygon, POINTS_ORDER, \
                                    reduce_lines, interpolate, group_lines
import pkg_resources as pkg
import sys

def test_order_points():
    assert list(POINTS_ORDER) == order_points(POINTS_ORDER)

    test_case = [(1, 1), (0, 1), (0, 0), (1, 0)]
    order = (2, 3, 0, 1)
    __assert_points_order(test_case, order, order_points(test_case))
    __assert_points_order(test_case, order, order_points(order_points(test_case)))

    test_case = [(10, 10), (0, 10), (0, 0), (10, 0)]
    order = (2, 3, 0, 1)
    __assert_points_order(test_case, order, order_points(test_case))
    __assert_points_order(test_case, order, order_points(order_points(test_case)))

    test_case = [(430, 130), (304, 33), (75, 100), (153, 272)]
    order = (2, 1, 0, 3)
    __assert_points_order(test_case, order, order_points(test_case))
    __assert_points_order(test_case, order, order_points(order_points(test_case)))

def test_ordered():
    test_case = [(1, 1), (0, 1), (0, 0), (1, 0)]
    expected = order_points(test_case)

    @ordered('toto', 'tata')
    def test(toto, tata=None):
        tata = tata or expected
        assert toto == expected
        assert tata == expected

    test(test_case)
    test(test_case, test_case)
    test(toto=test_case, tata=test_case)

def test_ordered_bubling_exception():
    try:
        order_points(90)
    except Exception as e:
        expected_exception = e

    @ordered('toto')
    def test(toto):
        pass

    try:
        test(90)
    except Exception as e:
        catched_exception = e

    assert type(expected_exception) == type(catched_exception)
    assert expected_exception.args == catched_exception.args


def __assert_points_order(points, order, actual):
    expected = [el[1] for el in sorted(list(zip(order, points)), key=lambda x: x[0])]
    assert expected == actual, "Wrong points order"


def test_distance():
    assert 1 == distance((0, 0), (0, 1))
    assert 5 == distance((0, 3), (4, 0))


def test_get_target_rectangle_size():
    test_case = ((0, 0), (1, 0), (0.5, 0.5), (0, 1))
    assert (1, 1) == get_target_rectangle_size(test_case)
    nparray = np.array(test_case, dtype='float')
    assert (1, 1) == get_target_rectangle_size(nparray)


def test_resize():
    array = np.ndarray(shape=(2000, 3000), dtype='uint8')
    try:
        resize(array)
        assert False, "should have raise exception"
    except ValueError as e:
        pass

    assert (200, 300) == resize(array, ratio=0.1).shape[:2]
    assert (200, 300) == resize(array, height=200).shape[:2]
    assert (200, 300) == resize(array, width=300).shape[:2]
    assert (220, 330) == resize(array, height=220, width=330).shape[:2]


def test_detect_englobing_polygon_simple():
    array = np.ones(shape=(5000, 5000, 3), dtype='uint8') * 250
    array[200:1800, 200:2800, :] = 0
    points = detect_englobing_polygon(array)
    assert len(points) == 4
    points = [tuple(*el) for el in points]
    assert (200, 200) in points
    assert (200, 1790) in points
    assert (2790, 200) in points
    assert (2790, 1790) in points


def test_detect_englobing_polygon_nested():
    array = np.ones(shape=(5000, 5000, 3), dtype='uint8') * 250
    array[200:1800, 200:2800, :] = 0
    array[300:1000, 400:2200, :] = 250
    points = detect_englobing_polygon(array)
    assert len(points) == 4
    points = [tuple(*el) for el in points]
    assert (200, 200) in points
    assert (200, 1790) in points
    assert (2790, 200) in points
    assert (2790, 1790) in points


def test_detect_englobing_polygon_error():
    array = np.ones(shape=(200, 200, 3), dtype='uint8') * 250
    try:
        points = detect_englobing_polygon(array)
        assert False, 'Detected points while no polygon in the image'
    except LookupError:
        pass


def test_detect_englobing_polygon_photo():
    array = _image('sheet.jpg')
    points = detect_englobing_polygon(array).astype(int)
    assert len(points) == 4
    area = cv2.contourArea(points)
    points = [(p[0, 0], p[0, 1]) for p in points]
    h, w = get_target_rectangle_size(points)
    assert h * w > (array.shape[0] * array.shape[1])* 1 / 3
    assert w > array.shape[0]/2
    assert h > array.shape[1]/2
    assert h * w > area

def test_reduce_lines():
    """test cases issued from lines.py on score_croped.jpg"""
    test_case = [((0, 25), (137, 25)),
                 ((0, 27), (137, 27)),
                 ((0, 34), (137, 34)),
                 ((0, 36), (137, 36)),
                 ((0, 43), (137, 43)),
                 ((0, 18), (137, 18)),
                 ((0, 16), (84, 16)),
                 ((8, 6),  (134, 8)),
                 ((51, 8), (137, 7))]
    assert len(list(reduce_lines(test_case, angle_threshold=0.1))) == 5

    test_case = [((-1000, 24), (999, 25)),
                 ((-1000, 26), (999, 27)),
                 ((-1000, 33), (999, 34)),
                 ((-1000, 35), (999, 36)),
                 ((-1000, 17), (999, 18)),
                 ((-1000, 15), (999, 16)),
                 ((-1000, 42), (999, 43)),
                 ((-999, 36), (1000, 1)),
                 ((-999, 34), (1000, 0)),
                 ((-1000, -11), (998, 57)),
                 ((-1000, -2), (998, 66)),
                 ((-998, 63), (1000, -5)),
                 ((-998, 72), (1000, 3)),
                 ((-999, 61), (1000, 26)),
                 ((-999, -20), (998, 48)),
                 ((-999, -11), (999, 23)),
                 ((-1000, 6), (999, 7)),
                 ((-1000, 24), (999, 59)),
                 ((-998, 54), (1000, -14)),
                 ((-993, 123), (999, -51))]
    assert len(list(reduce_lines(test_case))) == 5


def test_interpolate():
    assert interpolate((0, 0), (1, 0)) == (0, 0)
    assert interpolate((0, 0), (3000, 0)) == (0, 0)
    assert interpolate((0, 0), (1, 1)) == (1, 0)
    assert interpolate((0, 1), (1, 1)) == (0, 1)
    assert interpolate((0, 0), (0, 1)) == (sys.float_info.max, 0)

def test_group_lines():
    test_case = [((8, 6), (134, 8)), ((0, 16), (84, 16)), ((0, 25), (137, 25)), ((0, 34), (137, 34)), ((0, 43), (137, 43))]
    result = group_lines(test_case)
    assert len(result) == 1


    test_case =  [((-1000, 6), (999, 7)), ((-1000, 15), (999, 16)), ((-1000, 24), (999, 25)), ((-1000, 33), (999, 34)), ((-1000, 42), (999, 43))]
    result = group_lines(test_case)
    assert len(result) == 1


def _image(name):
    image = pkg.resource_stream('tests.images', name)
    array = np.asarray(bytearray(image.read()), dtype='uint8')
    assert array is not None
    return cv2.imdecode(array, cv2.IMREAD_UNCHANGED)
