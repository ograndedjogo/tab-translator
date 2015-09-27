# coding: utf-8


def order_points(points):
    ordered_points = [None for _ in range(4)]
    sorted_by_sum = sorted(points, key=lambda x: x[0] + x[1])
    sorted_by_diff = sorted(points, key=lambda x: x[0] - x[1])
    ordered_points[0] = sorted_by_sum[0]
    ordered_points[1] = sorted_by_diff[-1]
    ordered_points[2] = sorted_by_sum[-1]
    ordered_points[3] = sorted_by_diff[0]
    return ordered_points
