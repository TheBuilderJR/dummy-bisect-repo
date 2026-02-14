from fastmath import dot_product, euclidean_norm


def test_dot_product_basic():
    assert dot_product([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]) == 32.0


def test_dot_product_zeros():
    assert dot_product([0.0, 0.0], [5.0, 10.0]) == 0.0


def test_dot_product_single():
    assert dot_product([3.0], [7.0]) == 21.0


def test_euclidean_norm():
    assert euclidean_norm([3.0, 4.0]) == 5.0


def test_euclidean_norm_unit():
    assert euclidean_norm([1.0, 0.0, 0.0]) == 1.0
