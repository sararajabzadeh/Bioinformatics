string1 = input()
input()
t = input()
alph1 = t.split()
input()
string2 = input()
input()
t= input()
alph2 = t.split()
input()
input()
prob = [[]for i in range(len(alph2))]
# print(prob)
t=[]
for i in range(len(alph2)):
    t = input()
    prob[i] += t.split()
for i in range(len(alph2)):
    prob[i].pop(0)
for i in range(len(alph2)):
    for j in range(len(prob[0])):
        prob[i][j] = float(prob[i][j])
# print(prob)
# print(alph1)
# print(alph2)
result = 1
for i in range(len(string2)):
    index1 = alph2.index(string2[i])
    index2 = alph1.index(string1[i])
    result*=prob[index1][index2]
print(result)