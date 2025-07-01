# print below pattern
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 
alpha = ['A', 'B', 'C', 'D', 'E']

for i in range(len(alpha)):
    for j in range(i+1):
        print(alpha[j], end=" ")
    print()