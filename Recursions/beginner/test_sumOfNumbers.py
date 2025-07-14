import pytest
from sumOfNumbers import sumOfNumbers

test_data = [
    (0, 0),
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (5, 15),
    (6, 21)
]

@pytest.mark.parametrize("n, expected", test_data)
def test_sumOfNumbers(n, expected):
    assert sumOfNumbers(n) == expected, f"Test case for n={n} failed"
    print("All test cases passed!")