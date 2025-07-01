from powerOfNumber import powerOfNumber

def test_powerOfNumber():
    assert powerOfNumber(2, 0) == 1, "Test case 1 failed"
    assert powerOfNumber(2, 1) == 2, "Test case 2 failed"
    assert powerOfNumber(2, 2) == 4, "Test case 3 failed"
    assert powerOfNumber(2, 3) == 8, "Test case 4 failed"
    assert powerOfNumber(3, 3) == 27, "Test case 5 failed"
    assert powerOfNumber(5, 0) == 1, "Test case 6 failed"
    assert powerOfNumber(5, 1) == 5, "Test case 7 failed"
    assert powerOfNumber(5, 2) == 25, "Test case 8 failed"
    assert powerOfNumber(5, 5) == 3125, "Test case 9 failed"
    print("All test cases passed!")