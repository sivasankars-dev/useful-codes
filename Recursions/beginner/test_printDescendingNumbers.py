from printDescendingNumbers import printDescendingNumbers, printAscendingNumbers

def test_printDescendingNumbers():
    assert printDescendingNumbers(0) == [], "Test case 0 failed"
    assert printDescendingNumbers(1) == [1], "Test case 1 failed"  
    assert printDescendingNumbers(2) == [2, 1], "Test case 2 failed"
    assert printDescendingNumbers(3) == [3, 2, 1], "Test case 3 failed"
    assert printDescendingNumbers(4) == [4, 3, 2, 1], "Test case 4 failed"  
    assert printDescendingNumbers(5) == [5, 4, 3, 2, 1], "Test case 5 failed"
    assert printDescendingNumbers(6) == [6, 5, 4, 3, 2, 1], "Test case 6 failed"
    assert printDescendingNumbers(7) == [7, 6, 5, 4, 3, 2, 1], "Test case 7 failed"
    assert printDescendingNumbers(-5) == [], "Test case -5 failed"

    assert printDescendingNumbers(2) != [1,2], "Test case 2 failed"
    assert printDescendingNumbers(3) != [1,2,3], "Test case 3 failed" 
    assert printDescendingNumbers(4) != [1,2,3,4], "Test case 4 failed"
    assert printDescendingNumbers(5) != [1,2,3,4,5], "Test case 5 failed"
    assert printDescendingNumbers(6) != [1,2,3,4,5,6], "Test case 6 failed"
    assert printDescendingNumbers(7) != [1,2,3,4,5,6,7], "Test case 7 failed"
    print("All test cases passed!")


def test_printAscendingNumbers():
    assert printAscendingNumbers(0) == [], "Test case 0 failed"  
    assert printAscendingNumbers(1) == [1], "Test case 1 failed"
    assert printAscendingNumbers(2) == [1,2], "Test case 2 failed"
    assert printAscendingNumbers(3) == [1,2,3], "Test case 3 failed"
    assert printAscendingNumbers(4) == [1,2,3,4], "Test case 4 failed"
    assert printAscendingNumbers(5) == [1,2,3,4,5], "Test case 5 failed"

    assert printAscendingNumbers(-5) == [], "Test case 6 failed"
    print("All test cases passed!")