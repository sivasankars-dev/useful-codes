def customSlice(words, param1, param2):
    temp = ""
    for index, char in enumerate(words):
        if index >= param1 and param2 >= index:
            temp += char
            
    return temp
    
print(customSlice("Hello, World", 7, 12))