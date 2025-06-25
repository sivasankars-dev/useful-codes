# print below pattern
# A B C D E 
# A B C D 
# A B C 
# A B 
# A 

alpha = ['A', 'B', 'C', 'D', 'E']

for i in range(len(alpha), 0, -1):
    for j in range(i):
        print(alpha[j], end=" ")
    print()
