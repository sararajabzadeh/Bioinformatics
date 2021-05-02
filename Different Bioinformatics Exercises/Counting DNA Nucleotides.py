s = input()
A = 0
C = 0
G = 0
T = 0
array = []
for i in range(len(s)):
    if s[i] =="A":
        A+=1
    elif s[i]=="C":
        C +=1
    elif s[i]=="G":
        G +=1
    elif s[i]=="T":
        T +=1
array += [A]
array += [C]
array += [G]
array += [T]
print(*array , sep=" ")