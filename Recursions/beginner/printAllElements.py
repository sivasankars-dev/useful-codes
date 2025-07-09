# 🔹 7. Print all elements of an array
# Print all elements of an array using recursion.

# Input: [10, 20, 30]
# Output:
# 10
# 20
# 30

def printAllElements(arr):
    if len(arr) == 0:
        return
    print(arr[0])
    printAllElements(arr[1:])

printAllElements([10, 20, 30])  # Output: 10, 20, 30