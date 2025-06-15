# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 

for i in range(1, 6):
    flag = i%2
    for j in range(i):
        print(flag, end=' ')
        flag = 1 if flag == 0 else 0
    print()