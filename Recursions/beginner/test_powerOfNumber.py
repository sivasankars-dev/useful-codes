import pytest
from powerOfNumber import powerOfNumber

test_data = [   
    (2, 0, 1),
    (2, 1, 2),
    (2, 2, 4),
    (2, 3, 8),
    (3, 3, 27),
    (5, 0, 1),
    (5, 1, 5),
    (5, 2, 25),
    (5, 5, 3125)
]

@pytest.mark.parametrize("base, exponent, expected", test_data)
def test_powerOfNumber(base, exponent, expected):
    assert powerOfNumber(base, exponent) == expected, f"Test case for base={base}, exponent={exponent} failed"
    print("All test cases passed!")