# 6. Next Greater Element (Basic Version)
# ✔️ Difficulty: ⭐⭐
# Problem: For each element in an array, find the next greater element.
# Example:
# Input: [4, 5, 2, 25]
# Output: [5, 25, 25, -1]

# This solutin not solved yet.
def findNextGreaterElement(arr):
    result = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                result.append(arr[j])
                break
    else:
        result.append(-1)
    return result       



print(findNextGreaterElement([4,5,2,25]))
print(findNextGreaterElement([1, 2, 3, 4]))
print(findNextGreaterElement([4, 3, 2, 1]))
