#!/usr/bin/python
'''
This example illustrates how to use Hough Transform to find lines.
'''
import argparse
import numpy as np
import cv2
import math
from tabtranslator.transform import reduce_lines

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('image', help='path to the image file')
    args = ap.parse_args()

    src = cv2.imread(args.image)
    edged = cv2.Canny(src, 50, 200)
    greyed = cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR)
    hlines = HoughLines(edged)
    hlines = list(reduce_lines(hlines))
    hlinesp = HoughLinesP(edged)
    hlinesp = list(reduce_lines(hlinesp, angle_threshold=0.1))
    cv2.imshow('source', src)
    cv2.imshow('%d hlines' % len(hlines), print_lines(greyed, hlines))
    cv2.imshow('%d hlinesp' % len(hlinesp), print_lines(greyed, hlinesp))
    cv2.imshow('skeleton', skeletonize(src))
    cv2.waitKey(0)

def print_lines(image, lines):
    result = image.copy()
    for point1, point2 in lines:
        cv2.line(result, point1, point2, (0, 0, 255), 3, cv2.LINE_AA)
    return result

def HoughLinesP(image):
    lines = cv2.HoughLinesP(image, 1, math.pi/180.0, 40, np.array([]), 50, 10)
    lines_points = []
    for [[x1, y1, x2, y2]] in lines:
        lines_points.append(((x1, y1), (x2, y2)))
    return lines_points

def HoughLines(image):
    lines = cv2.HoughLines(image, 1, math.pi/180.0, 50, np.array([]), 0, 0)
    lines_points = []
    for [[rho, theta]] in lines:
        a = math.cos(theta)
        b = math.sin(theta)
        x0, y0 = a*rho, b*rho
        pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
        pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
        lines_points.append((pt1, pt2))
    return lines_points

def skeletonize(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    size = np.size(image)
    skeleton = np.zeros(image.shape,np.uint8)
    ret,image = cv2.threshold(image,127,255,0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    done = False
    while(not done):
        eroded = cv2.erode(image,element)
        temp = cv2.dilate(eroded,element)
        temp = cv2.subtract(image,temp)
        skeleton = cv2.bitwise_or(skeleton,temp)
        image = eroded.copy()
        zeros = size - cv2.countNonZero(image)
        if zeros==size:
            done = True
    return skeleton

if __name__ == '__main__':
    main()
