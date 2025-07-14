import pytest
from printDescendingNumbers import printDescendingNumbers, printAscendingNumbers

decending_test_data = [
    (0, []),
    (1, [1]),
    (2, [2, 1]),    
    (3, [3, 2, 1]),
    (4, [4, 3, 2, 1]),
    (5, [5, 4, 3, 2, 1]),
    (6, [6, 5, 4, 3, 2, 1]),
    (7, [7, 6, 5, 4, 3, 2, 1]),
    (8, [8, 7, 6, 5, 4, 3, 2, 1]),
    (9, [9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (11, [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (12, [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (13, [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (14, [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (15, [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    (-5, []),  
]

ascending_test_data = [
    (0, []),
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 2, 3]),
    (4, [1, 2, 3, 4]),
    (5, [1, 2, 3, 4, 5]),
    (6, [1, 2, 3, 4, 5, 6]),
    (-5, []), 
    (7, [1, 2, 3, 4, 5, 6, 7]),
    (8, [1, 2, 3, 4, 5, 6, 7, 8]),
    (9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    (11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    (12, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    (13, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
    (14, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]),
    (15, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
]

@pytest.mark.parametrize("n, expected", decending_test_data)
def test_printDescendingNumbers(n, expected):
    assert printDescendingNumbers(n) == expected, f"Test case for n={n} failed"
    print("All test cases passed!")

@pytest.mark.parametrize("n, expected", ascending_test_data)
def test_printAscendingNumbers(n, expected):
    assert printAscendingNumbers(n) == expected, f"Test case for n={n} failed"
    print("All test cases passed!")