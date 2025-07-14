import pytest
from checkArraySorted import sortedArray

test_data = [
    ([1, 2, 3, 4, 5], True),
    ([1, 2, 2, 4], False),
    ([5, 6, 7, 8], True),
    ([1, 3, 2], False),
    ([1], True),
    ([], True),
    ([1, 2, 3, 4, 5, 6], True),
    ([10, 20, 30, 40], True),
    ([1, 2, 3, 2], False),
    ([2, 2, 2], False),
    ([3, 2, 1], False),
    ([1, 2, 3, 4, 5, 6, 7], True),
    ([5, 4, 3, 2, 1], False),
    ([10, 20, 30, 20], False),
    ([1, 2, 3, 4, 5, 6, 7, 8], True),
    ([8, 7, 6, 5], False),
    ([1.1, 2.2, 3.3], True),
    ([3.3, 2.2, 1.1], False),
    ([1000, 2000, 3000], True),
    ([3000, 2000, 1000], False)
]

@pytest.mark.parametrize("input_array, expected", test_data)
def test_checkArraySorted(input_array, expected):
    assert sortedArray(input_array) == expected