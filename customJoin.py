def customJoin(arr, sep):
    res = ""
    for index, char in enumerate(arr):
        if index == len(arr)-1:
            res += char
        else:
            res += char+sep
    return res


print(customJoin(['Hello', 'world', 'siva'], ' '))