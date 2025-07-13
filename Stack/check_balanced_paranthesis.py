# Difficulty: ⭐⭐
# Problem: Check if a string contains balanced parentheses.
# Examples:
# Input: "(())"
# Output: True

# Input: "(()"
# Output: False
def checkBalancedParenthesis(string):
    stack = []
    mapping = {')':'(', ']': '[', '}': '{'}

    for ch in string:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            return False
    
    return not stack

print(checkBalancedParenthesis("(())"))
print(checkBalancedParenthesis("{}()[]"))
print(checkBalancedParenthesis("((])"))
print(checkBalancedParenthesis("(())"))
print(checkBalancedParenthesis("(()"))
print(checkBalancedParenthesis("{[()]}"))
print(checkBalancedParenthesis("{[[]]}"))
print(checkBalancedParenthesis("{[()]}))"))
print(checkBalancedParenthesis("{[(]]}"))
print(checkBalancedParenthesis("{[(])]}"))