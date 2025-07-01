# 🔹 2. Sum of first N natural numbers
# Write a recursive function to calculate the sum from 1 to n.

# Input: n = 5
# Output: 15 (1 + 2 + 3 + 4 + 5)

n = 6

def sumOfNumbers(n):
    if n == 0:
        return 0
    return n + sumOfNumbers(n - 1)

print(f"Sum of first {n} natural numbers is: {sumOfNumbers(n)}")