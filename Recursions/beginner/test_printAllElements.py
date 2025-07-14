import pytest
from printAllElements import printAllElements

test_data = [
    ([10, 20, 30], None),
    ([], None),
    ([1], None),
    ([1, 2, 3], None),
    ([5, 10, 15, 20], None),
    ([100, 200], None),
    ([42], None),
    ([0], None),
    ([1, 2], None),
    ([3, 4, 5], None),
    ([10, 20, 30, 40], None),
    ([1000], None),
    ([7, 14, 21], None),
    ([9, 18], None),
    ([11, 22, 33], None),
    ([5, 10, 15], None),
    ([100, 200, 300], None),
    ([1, 3, 5, 7], None),
    ([2, 4, 6, 8], None),
    ([12, 24, 36], None),
    ([15, 30], None),
    ([8, 16, 24], None),
    ([13, 26, 39], None),
    ([4, 8, 12], None),
    ([6, 12, 18], None),
    ([3, 6, 9], None),
    ([2, 5, 8], None),
    ([1, 4, 7], None),
    ([0, 1, 2], None),
]

@pytest.mark.parametrize("input_array, expected", test_data)
def test_printAllElements(input_array, expected):
    assert printAllElements(input_array) == expected, f"Test case for input_array={input_array} failed"
    print("All test cases passed!")

    