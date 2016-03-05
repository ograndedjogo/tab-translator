from tabtranslator.transform import (detect_englobing_polygon, resize,
                                    ordered, get_target_rectangle_size,
                                    POINTS_ORDER)
import argparse
import numpy as np
import cv2

def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("image", help="path to the image file")
    args = ap.parse_args()

    image = cv2.imread(args.image)
    image = resize(image, width=2000)
    pts = detect_englobing_polygon(image)
    pts = [tuple(*el) for el in pts]
    warped = wrap_perspective(image, pts)

    pts = np.array(pts, np.int32)
    pts = pts.reshape((-1,1,2))
    image = cv2.polylines(image,[pts],True,(0,255,255), 10)
    cv2.imshow("Original", resize(image, width=1000))
    cv2.imshow("Warped", resize(warped, width=1000))
    cv2.waitKey(0)

@ordered('points')
def wrap_perspective(image, points):
    width, height = get_target_rectangle_size(points)
    expected_points = [(el[0] * width, el[1] * height) for el in POINTS_ORDER]

    # get the transform matrice and apply it to the image
    np_points = [np.array(p, dtype='float32')
                 for p in (points, expected_points)]
    matrice = cv2.getPerspectiveTransform(*np_points)
    return cv2.warpPerspective(image, matrice, (width, height))


if __name__ == '__main__':
    main()
