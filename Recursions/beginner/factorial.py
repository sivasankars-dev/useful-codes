# 🔹 3. Factorial of N
# Classic recursion problem.

# Input: n = 5
# Output: 120 (5 × 4 × 3 × 2 × 1)

n = 2

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

print(f"factorial of {n} is: {factorial(n)}")