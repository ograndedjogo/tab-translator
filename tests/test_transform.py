from tabtranslator.transform import order_points


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
