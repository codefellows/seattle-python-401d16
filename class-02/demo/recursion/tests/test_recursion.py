from recursion_package.recursion_module import factorial, reverse_list


def test_factorial_one():
    actual = factorial(1)
    expected = 1
    assert actual == expected


def test_factorial_two():
    actual = factorial(2)
    expected = 2
    assert actual == expected


def test_factorial_5():
    actual = factorial(5)
    expected = 120
    assert actual == expected


def test_reverse_list_even():
    actual = reverse_list([1, 2, 3, 4])
    expected = [4, 3, 2, 1]
    assert actual == expected


def test_reverse_list_odd():
    actual = reverse_list([1, 2, 3])
    expected = [3, 2, 1]
    assert actual == expected


def test_reverse_single():
    actual = reverse_list([1])
    expected = [1]
    assert actual == expected


def test_reverse_empty():
    actual = reverse_list([])
    expected = []
    assert actual == expected
