# Searching substring
def customFind(words, findSubStr):
    substrArr = words.split(' ')
    for substr in substrArr:
        if substr == findSubStr:
            return words.index(substr)
            
    # or we can use simplest this method
    # return words.index(findSubStr)

# print(customFind('Look for the substring in the string', 'substring'))