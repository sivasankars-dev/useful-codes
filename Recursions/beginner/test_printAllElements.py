from printAllElements import printAllElements

def test_printAllElements():
    assert printAllElements([10, 20, 30]) == None, "Test case 1 failed"
    assert printAllElements([]) == None, "Test case 2 failed"       
    assert printAllElements([1]) == None, "Test case 3 failed"
    assert printAllElements([1, 2, 3]) == None, "Test case 4 failed"                
    assert printAllElements([5, 10, 15, 20]) == None, "Test case 5 failed"
    assert printAllElements([100, 200]) == None, "Test case 6 failed"
    assert printAllElements([42]) == None, "Test case 7 failed"
    assert printAllElements([0]) == None, "Test case 8 failed"
    assert printAllElements([1, 2]) == None, "Test case 9 failed"
    assert printAllElements([3, 4, 5]) == None, "Test case 10 failed"
    assert printAllElements([10, 20, 30, 40]) == None, "Test case 11 failed"
    assert printAllElements([1000]) == None, "Test case 12 failed"
    assert printAllElements([7, 14, 21]) == None, "Test case 13 failed"
    assert printAllElements([9, 18]) == None, "Test case 14 failed"
    assert printAllElements([11, 22, 33]) == None, "Test case 15 failed"
    assert printAllElements([5, 10, 15]) == None, "Test case 16 failed"
    print("All test cases passed!")

    