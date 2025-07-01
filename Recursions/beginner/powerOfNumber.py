# 🔹 4. Power of a number
# Write a function to compute a^b (e.g., 2³ = 8).

# Input: a = 2, b = 3
# Output: 8

def powerOfNumber(a, b):
    if b == 0:
        return 1
    return a * powerOfNumber(a, b -1)

print(f"Power of {2} raised to {3} is: {powerOfNumber(2, 3)}")