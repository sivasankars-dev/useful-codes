# 🔹 6. Reverse a string
# Use recursion to reverse a string.

# Input: "siva"
# Output: "avis"

def reverseString(s):
    if len(s) == 0:
        return s
    return s[-1] + reverseString(s[:-1])

print(reverseString("siva"))  # Output: "avis"
