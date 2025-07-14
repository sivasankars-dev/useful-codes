import pytest
from factorial import factorial

test_data = [
    (1, 1),
    (0, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880),
    (10, 3628800),
    (11, 39916800),
    (12, 479001600),
    (13, 6227020800),
    (14, 87178291200),
    (15, 1307674368000),
    (16, 20922789888000),
    (17, 355687428096000),
    (18, 6402373705728000),
    (19, 121645100408832000),
    (20, 2432902008176640000),
    # # Edge cases
    # (-1, "Error: Factorial is not defined for negative numbers"),
    # (100, "Error: Factorial is too large to compute"),
    # (50, 3041409320171337804361269007),  # Example of a large factorial
    # (25, 15511210043330985984000000)  # Example of a moderately large factorial
]

@pytest.mark.parametrize("input_data, expected", test_data)
def test_factorial(input_data, expected):
    assert factorial(input_data) == expected
    print("All test cases passed!")