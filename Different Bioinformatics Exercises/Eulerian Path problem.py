import copy
t = ""
array = []
m=0
while t!="*":
    t = input()
    array += [t.split(" -> ")]
array.remove(array[len(array)-1])
# print(array)
array1 =[]
array2=[]
array2prime= []
for i in range(len(array)):
        array1+=[array[i][0]]
        array2+=array[i][1:]
# print(array1)
for i in range(len(array1)):
    array1[i] = int(array1[i])
# print(array1)
# print(max(array1))
# print(array2)
for i in range(len(array2)):
    array2prime += [array2[i].split(",")]
# print(array2prime)

for i in range(len(array2prime)):
    for j in range(len(array2prime[i])):
        array2prime[i][j] = int(array2prime[i][j])
# print(array2prime)

array3 = [[]for i in range(max(array1)+1)]

inNode = [0]*(max(array1)+1)
outNode = [0]*(max(array1)+1)
# print(array1)
# print(array2prime)
# print(outNode)
# print(inNode)
for i in range(len(array2prime)):
    for j in range(len(array2prime[i])):
        inNode[array2prime[i][j]] +=1
        outNode[array1[i]] += 1
        # print("in")
# print(inNode)
        # print("out")
# print(outNode)

for i in range(len(inNode)):
    if inNode[i]-outNode[i]==-1:
        node = i
# print(node)

for i in range(len(array1)):
    array3[array1[i]] = array2prime[i]

count = 0
for i in range(len(array3)):
    for j in range(len(array3[i])):
        count+=1

temp = copy.deepcopy(array3)
av = []
ola = copy.deepcopy(array3)
for i in range(len(array3)):
    for j in range(len(array3[i])):
        ola[i][j] = 1
# print(olagh)
def khab(node , temp,count , av , ola):

    for i in range(len(temp[node])):

        if ola[node][i] != -1:
            ola[node][i] = -1
            khab(temp[node][i] , temp , count , av , ola)
    av += [node]
    return av
out = khab(node , temp , count , av , ola)
out2 = []
for i in range(len(out)-1 , -1 , -1):
    out2+=[out[i]]
res= []
for i in range(len(out2)):
    if i==len(out2)-1:
        res+=[out2[len(out2)-1]]
    else:
        res+= [out2[i]]
        res+=["->"]
print(*res, sep="")