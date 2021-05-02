import math
string = input()
text = input().split()
array = [0]
for i in range(len(text)):
    array += [int(text[i])]
k = int(input())
# print(string)
# print(array)
# print(k)

integerMassTable = {"G" :57,
                    "A":71,
                    "S":87,
                    "P":97,
                    "V":99,
                    "T":101,
                    "C":103,
                    "I":113,
                    "L":113,
                    "N":114,
                    "D":115,
                    "K":128,
                    "Q":128,
                    "E":129,
                    "M":131,
                    "H":137,
                    "F":147,
                    "R":156,
                    "Y":163,
                    "W":186,
                    "X":4,
                    "Z":5}
# print(integerMassTable)

diffArray = [1]
for i in string:
    for j in integerMassTable:
        # print(len(integerMassTable))
        if j == i:
            diffArray+=[integerMassTable[j]]
            continue


# print(diffArray)


indexarray = [0]
for i in range(1,len(diffArray)):
        indexarray+=[diffArray[i]+indexarray[i-1]]



# print(indexarray)
# indexarray.pop(0)



arrayscore = [0]
for i in range(1,len(diffArray)):
        arrayscore+=[indexarray[i]-1]
# print(arrayscore)

score = 0
for i in range(len(array)):
    if i!=0 and i in indexarray:
        score+=array[i]
# print(score)

firstScore = [0]*(len(array)-1)

for i in range(len(firstScore)):
    if i!= 0 and i in arrayscore:
        firstScore[i]=1
# print(firstScore)


layers = [[[-math.inf for i in range(k+1)]for j in range(len(array))]for l in range(len(string)+1)]
backtrack =[[[() for i in range(k+1)]for j in range(len(array))]for l in range(len(string)+1)]

# print(layers[0][0])
layers[0][0][0] = 0
count = 0
for i in range(1,len(string)+1):
    # print("isdcoasjkdiahsias")
    # print(len(layers[0]))
    # print(i)
    count=0
    for j in range(i,len(array)):
        # print("j")
        # print(j)
        # for l in range(len(diffArray)):
        # print(diffArray[count])
        # print(array[j])
        # print(layers[i-1][j-diffArray[count]][0])
        if j!=1 and j in indexarray:
            count+=1
        # print(count)
        if j!= 1 and j in indexarray:
            layers[i][j][0] = layers[i-1][j-diffArray[i]][0]+array[j]
            backtrack[i][j][0] = (i-1 , j-diffArray[i] , 0)

        # print(j)
        # backtrack[i][j][0]
        # if j in indexarray and indexarray[count]==j:
        #     # if j==0:
        #     #     count+=1
        #     #     break
        #     # print(layers[0])
        #     layers[i][j][0]=layers[i-1][j-diffArray[i]][0] + array[j]
        #     # layers[i][j][0]=1
        #     count+=1
        #     # print(count)
        # print("javab")
        # print(layers[i][j][0])
# print(backtrack)
# print(layers)
        #     break



count = 1
m = -math.inf
for l in range(1,k+1):
    for i in range(1,len(string)+1):

        # print("tammmmannammsdmmsd")

        count = 1
        for j in range(1,len(array)):
            m = -math.inf
            if j!=1 and j in diffArray:
                count+=1
            for temp in range(j):
                # print("salam")
                # print(diffArray[count])
                if layers[i-1][temp][l-1]>m:
                    m = layers[i-1][temp][l-1]
                    indices = (i-1, temp , l-1)
                    # print("m")
                    # print(m)
            # print("diff")
            # print(diffArray[i])
            # print("count")
            # print(count)
            # print(layers[i-1][j-diffArray[i]][l])
            if j > diffArray[i]:
                maximum = max(m , layers[i-1][j-diffArray[i]][l])
                if maximum!=m:
                    indices = (i-1,j-diffArray[i],l)
            else:
                maximum = m
                # indices = (i-1,temp)
            # if maximum!= m:
            #     indices = (i-1,j-diffArray[count],l)
            # print("i")
            # print(i)
            # print("j")
            # print(j)
            # print("max")
            # print(maximum)
            layers[i][j][l] = maximum + array[j]
            backtrack[i][j][l]= indices
            # print("javab")
            # print(layers[i][j][l])
# print(layers)
# print(backtrack)






i = len(string)
j = len(array)-1
l = k
result = [0]
# print(i , j , k)

# print(backtrack[3][14][2][2])
while i!=0 and j != 0:
    # print("Hellp")
    result += [j]
    # print(result)
    temp1 = backtrack[i][j][l][0]

    temp2 = backtrack[i][j][l][1]

    temp3 = backtrack[i][j][l][2]
    i = temp1
    j = temp2
    l = temp3
    print("i")
    print(i)
    print("j")
    print(j)
    print("l")
    print(l)


# for i in range(len(result)):
#     result[i] -= 1
result+=[0]
print(result)


diffArray2 = []

for i in range(len(result)-2,0,-1):
    diffArray2 += [result[i]-result[i+1]]
diffArray.pop(0)
print(diffArray)
print(diffArray2)

stringAkhar = ""

print(len(string))
print(len(diffArray2))


for i in range(len(diffArray2)):
    if diffArray[i]==diffArray2[i]:
        stringAkhar+=string[i]
    elif diffArray2[i] > diffArray[i]:
        stringAkhar += string[i]
        stringAkhar += "(+"
        stringAkhar+= str(diffArray2[i]-diffArray[i])
        stringAkhar += ")"
    elif diffArray2[i] < diffArray[i]:
        stringAkhar+=string[i]
        stringAkhar+="("
        stringAkhar+=str(diffArray2[i]-diffArray[i])
        stringAkhar+=")"

print(stringAkhar)



# final = [0]*(len(array)-1)
# for i in range(len(final)):
#     if i in result:
#         final[i] =1
# print(final)





# count0 = 0
# count1 = 0
# count00 = []
# count11 = []
# print(len(firstScore))
# print(len(final))
# print(len(result))

# khar = 0
# for i in range(len(final)):
#     if final[i]==1:
#         khar+=1
# print("khar")
# print(khar)
#
# khar = 0
# for i in range(len(firstScore)):
#     if firstScore[i]==1:
#         khar+=1
# print("khar")
# print(khar)






# for i in range(len(final)):
#     if firstScore[i]==0:
#         count0+=1
#     elif firstScore[i]==1:
#         # print("count0")
#         # print(count0)
#         count00+=[count0]
#         count0 = 0
# for i in range(len(final)):
#     if final[i]==0:
#         count1 +=1
#     elif final[i] ==1:
#         # print("count1")
#         # print(count1)
#         count11 += [count1]
#         count1 = 0
# print(count00)
# print(count11)






# javab = ""
# for i in range(len(string)):
#     if count00[i]==count11[i]:
#         javab += string[i]
#     elif count11[i]-count00[i]<0:
#         javab+=string[i]
#         javab+="("
#         javab+=str(count11[i]-count00[i])
#         javab+=")"
#     elif count11[i]-count00[i]>0:
#         javab += string[i]
#         javab += "(+"
#         javab += str(count11[i] - count00[i])
#         javab += ")"
# if len(count00) < len(string):
#     for i in range(len(string)-len(count00)):
#         javab+=string[len(count00)+i]
#
# print(javab)