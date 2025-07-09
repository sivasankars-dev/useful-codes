from reverseString import reverseString

def test_reverseString():
    assert reverseString("siva") == "avis", "Test case 1 failed"
    assert reverseString("hello") == "olleh", "Test case 2 failed"
    assert reverseString("world") == "dlrow", "Test case 3 failed"
    assert reverseString("python") == "nohtyp", "Test case 4 failed"        
    assert reverseString("recursion") == "noisrucer", "Test case 5 failed"
    assert reverseString("test") == "tset", "Test case 6 failed"
    assert reverseString("12345") == "54321", "Test case 7 failed"
    assert reverseString("a") == "a", "Test case 8 failed"
    assert reverseString("") == "", "Test case 9 failed"
    assert reverseString("madam") == "madam", "Test case 10 failed"
    assert reverseString("level") == "level", "Test case 11 failed"
    assert reverseString("radar") == "radar", "Test case 12 failed"
    assert reverseString("civic") == "civic", "Test case 13 failed"
    assert reverseString("noon") == "noon", "Test case 14 failed"
    assert reverseString("kayak") == "kayak", "Test case 15 failed"
    assert reverseString("deified") == "deified", "Test case 16 failed"
    assert reverseString("rotor") == "rotor", "Test case 17 failed"
    assert reverseString("refer") == "refer", "Test case 18 failed"
    assert reverseString("level") == "level", "Test case 19 failed"
    assert reverseString("madam") == "madam", "Test case 20 failed"
    print("All test cases passed!")
    
