# 🔹 5. Check if array is sorted (strictly increasing)
# Given an array, check if it is sorted in strictly increasing order.

# Input: [1, 2, 3, 4, 5]
# Output: True
# Input: [1, 2, 2, 4]
# Output: False

def sortedArray(arr, index=0):
    if len(arr) < 2:
        return True
    if index == len(arr) - 1:
        return True
    if arr[index] >= arr[index + 1]:
        return False
    return sortedArray(arr, index + 1)
    

print(sortedArray([1, 2, 3, 4, 5]))  # Output: True