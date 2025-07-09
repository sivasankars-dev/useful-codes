# 🔹 8. Find Nth Fibonacci number
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...

# Input: n = 5
# Output: 5 (fib(5) = 5)

def NthFib(findPos, arr = [0,1], pos=1):
  if findPos < pos:
    return arr[pos-1]
  res = arr[-1]+arr[-2]
  arr.append(res)
  return NthFib(findPos, arr, pos+1)
  
print(NthFib(1))