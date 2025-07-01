from factorial import factorial

def test_factorial():
    assert factorial(1) == 1, "Test case 1 failed"
    assert factorial(0) == 1, "Test case 0 failed (0! is defined as 1)"
    assert factorial(2) == 2, "Test case 2 failed"
    assert factorial(3) == 6, "Test case 3 failed"
    assert factorial(4) == 24, "Test case 4 failed"
    assert factorial(5) == 120, "Test case 5 failed"
    assert factorial(6) == 720, "Test case 6 failed"
    assert factorial(7) == 5040, "Test case 7 failed"
    assert factorial(8) == 40320, "Test case 8 failed"
    print("All test cases passed!")