# Remove Adjacent Duplicate Characters from a String
# ✔️ Difficulty: ⭐⭐
# Problem: Remove adjacent duplicates using a stack.
# Example:
# Input: "abbaca"
# Output: "ca"

def removeAdjacentDuplicates(string):
    removedDuplicates = ""

    for ch in string:
        if not removedDuplicates or ch != removedDuplicates[-1]:
            removedDuplicates += ch
        else:
            removedDuplicates = removedDuplicates[:-1]
    
    return removedDuplicates

print(removeAdjacentDuplicates('abbaca'))


