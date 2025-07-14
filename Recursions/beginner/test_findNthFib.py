import pytest
from findNthFib import NthFib

test_data = [
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (0, 0),
    (11, 89),
    (12, 144)
]

@pytest.mark.parametrize("n, expected", test_data)
def test_findNthFib(n, expected):
    assert NthFib(n) == expected, f"Test case for n={n} failed"
    print("All test cases passed!")