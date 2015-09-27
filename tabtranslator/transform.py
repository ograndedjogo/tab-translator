# coding: utf-8
import numpy as np


def order_points(points):
    ordered_points = [None for _ in range(4)]
    sorted_by_sum = sorted(points, key=lambda x: x[0] + x[1])
    sorted_by_diff = sorted(points, key=lambda x: x[0] - x[1])
    ordered_points[0] = sorted_by_sum[0]
    ordered_points[1] = sorted_by_diff[-1]
    ordered_points[2] = sorted_by_sum[-1]
    ordered_points[3] = sorted_by_diff[0]
    return ordered_points


def distance(point_a, point_b):
    x_diff = point_a[0] - point_b[0]
    y_diff = point_a[1] - point_b[1]
    return np.sqrt(x_diff ** 2 + y_diff ** 2)
