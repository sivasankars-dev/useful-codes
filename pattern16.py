# print below pattern
# A 
# B B 
# C C C 
# D D D D 
# E E E E E 


alpha = ['A', 'B', 'C', 'D', 'E']
for i in range(len(alpha)):
    for j in range(i+1):
        print(alpha[i], end=" ")
    print()