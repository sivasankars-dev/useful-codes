from findNthFib import NthFib

def test_findNthFib():
    assert NthFib(5) == 5, "Test case 1 failed" 
    assert NthFib(6) == 8, "Test case 2 failed"
    assert NthFib(7) == 13, "Test case 3 failed"
    assert NthFib(8) == 21, "Test case 4 failed"
    assert NthFib(9) == 34, "Test case 5 failed"
    assert NthFib(10) == 55, "Test case 6 failed"
    assert NthFib(1) != 0, "Test case 7 failed"
    assert NthFib(2) == 1, "Test case 8 failed"
    assert NthFib(3) != 1, "Test case 9 failed"
    assert NthFib(4) != 2, "Test case 10 failed"
    assert NthFib(0) == 0, "Test case 11 failed (n=0)"
    assert NthFib(11) == 89, "Test case 12 failed"
    assert NthFib(12) == 144, "Test case 13 failed"
    print("All test cases passed!")