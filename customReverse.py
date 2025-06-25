def customReverse(reverseCharacters):
    typeOfInputs = "" if isinstance(reverseCharacters, str) else []
    
    for i in range(len(reverseCharacters)-1, -1, -1):
        if isinstance(typeOfInputs, str):
            typeOfInputs += reverseCharacters[i]
        else:
            typeOfInputs.append(reverseCharacters[i])
        
    return typeOfInputs
            
        
print(customReverse([1,2,3,4,5]))
print(customReverse("Hello"))