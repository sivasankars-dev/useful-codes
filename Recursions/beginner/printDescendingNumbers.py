# 1. Print numbers inside List from N to 1

n = 2
def printDescendingNumbers(n):
    if n == 0 or n < 0:
        return []
    return [n] + printDescendingNumbers(n - 1)

print(f"Descending Numbers from N to 1: {printDescendingNumbers(n)}")

# 2. Print numbers inside List from 1 to N
def printAscendingNumbers(n, current=n-(n-1)):
    if current > n:
        return []
    return [current] + printAscendingNumbers(n, current + 1)

print(f"\nAscending Numbers from 1 to N: {printAscendingNumbers(n)}")