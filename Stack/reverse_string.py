def reverseString(s):
    originalStringList = list(s)
    reverse = ""
    while originalStringList:
        reverse += originalStringList.pop()
    
    return reverse

print(reverseString('siva'))