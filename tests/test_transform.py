import numpy as np
import cv2
from tabtranslator.transform import order_points, distance, get_target_rectangle_size, resize, detect_englobing_polygon


def test_order_points():
    test_case = [(1, 1), (0, 1), (0, 0), (1, 0)]
    order = (2, 3, 0, 1)
    __assert_points_order(test_case, order, order_points(test_case))

    test_case = [(10, 10), (0, 10), (0, 0), (10, 0)]
    order = (2, 3, 0, 1)
    __assert_points_order(test_case, order, order_points(test_case))

    test_case = [(10, 9), (1, 10), (1, 0.5), (8, 0)]
    order = (2, 3, 0, 1)
    __assert_points_order(test_case, order, order_points(test_case))

def __assert_points_order(points, order, actual):
    expected = [el[1] for el in sorted(list(zip(order, points)), key=lambda x: x[0])]
    assert expected == actual, "Wrong points order"


def test_distance():
    assert 1 == distance((0, 0), (0, 1))
    assert 5 == distance((0, 3), (4, 0))

def test_get_target_rectangle_size():
    test_case = ((0, 0), (1, 0), (0.5, 0.5), (0, 1))
    assert (1, 1) == get_target_rectangle_size(test_case)


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

def test_detect_englobing_polygon():
    array = np.ones(shape=(2000, 3000, 3), dtype='uint8') * 250
    array[200:1800, 200:2800, :] = 0
    array[300:1000, 400:2200, :] = 250
    points = detect_englobing_polygon(array)
    assert len(points) == 4
    assert (200, 200) in points
    assert (200, 1799) in points
    assert (2799, 200) in points
    assert (2799, 1799) in points


