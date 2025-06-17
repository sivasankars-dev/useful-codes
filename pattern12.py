# Can you print below pattern
# 1             1 
# 1 2         2 1 
# 1 2 3     3 2 1 
# 1 2 3 4 4 3 2 1 

n = 4
for i in range(n):
    for j in range(n):
        if i >= j:
            print(j+1, end=" ")
        else:
            print(" ", end=" ")

    for k in range(n):
        if n-1-i <= k:
            print(n-1-k+1, end=" ")
        else:
            print(" ", end=" ")
    print()