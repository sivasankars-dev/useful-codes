from sumOfNumbers import sumOfNumbers

def test_sumOfNumbers():
    assert sumOfNumbers(0) == 0, "Test case 1 failed"
    assert sumOfNumbers(1) == 1, "Test case 2 failed"
    assert sumOfNumbers(2) == 3, "Test case 3 failed"
    assert sumOfNumbers(3) == 6, "Test case 4 failed"
    assert sumOfNumbers(4) == 10, "Test case 5 failed"
    assert sumOfNumbers(5) == 15, "Test case 6 failed"
    assert sumOfNumbers(6) == 21, "Test case 7 failed"
    print("All test cases passed!")