from checkArraySorted import sortedArray

def test_checkArraySorted():
    assert sortedArray([1, 2, 3, 4, 5]) == True, "Test case 1 failed"
    assert sortedArray([1, 2, 2, 4]) == False, "Test case 2 failed"
    assert sortedArray([5, 6, 7, 8]) == True, "Test case 3 failed"
    assert sortedArray([1, 3, 2]) == False, "Test case 4 failed"
    assert sortedArray([1]) == True, "Test case 5 failed"
    assert sortedArray([]) == True, "Test case 6 failed (empty array)"
    assert sortedArray([1, 2, 3, 4, 5, 6]) == True, "Test case 7 failed"
    assert sortedArray([10, 20, 30, 40]) == True, "Test case 8 failed"
    assert sortedArray([1, 2, 3, 2]) == False, "Test case 9 failed"
    assert sortedArray([2, 2, 2]) == False, "Test case 10 failed (all elements equal)"
    print("All test cases passed!")