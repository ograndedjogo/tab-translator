from tabtranslator.transform import order_points, detect_englobing_polygon, process, resize
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
    warped = process(image, pts)

    pts = np.array(pts, np.int32)
    pts = pts.reshape((-1,1,2))
    image = cv2.polylines(image,[pts],True,(0,255,255), 10)
    cv2.imshow("Original", resize(image, width=1000))
    cv2.imshow("Warped", resize(warped, width=1000))
    cv2.waitKey(0)


if __name__ == '__main__':
    import os
    print(os.getcwd())
    main()
