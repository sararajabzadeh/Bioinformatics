import copy
theta , sigma = map(float,input().split())
# print(sigma)
input()
alphabet = input().split()
input()
temp = input()
align = []
while temp!="*":
    align += [temp]
    temp = input()
# print(theta)
# print(alphabet)
# print(align)
n = len(align)
m = len(align[0])
matchOrInsert = []
for i in range(m):
    sum = 0
    for j in range(n):
        if align[j][i]== "-":
            sum+=1
    if sum/n <= theta:
        matchOrInsert += ["MD"]
    else:
        matchOrInsert += ["Ins"]
# print(matchOrInsert)
MIndex = 0
iIndex = 0
matrix = [["-" for i in range(m)] for j in range(n)]
# print(matrix)
for i in range(m):
    if matchOrInsert[i] == "MD":
        MIndex += 1
        iIndex += 1
        for j in range(n):
            if align[j][i] == "-":
                matrix[j][i] = "D"+str(MIndex)
            else:
                matrix[j][i] = "M"+str(MIndex)
    else:
        for j in range(n):
            if align[j][i] != "-":
                matrix[j][i] = "I"+str(iIndex)
# print(matrix)
InsCount = 0
for i in range(m):
    if matchOrInsert[i] == "Ins":
        InsCount +=1
probability = {"S":{"I0":0,"M1":0,"D1":0}}
for i in range(m-InsCount+1):
    if i == m-InsCount:
        probability["I" + str(i)] = {"I" + str(i): 0,"E":0}
    else:
        probability["I"+str(i)] = {"I"+str(i):0,"M"+str(i+1):0,"D"+str(i+1):0}
    if i < m-InsCount:
        if i==m-InsCount-1:
            probability["M" + str(i + 1)] = {"I" + str(i + 1): 0,"E":0}
            probability["D" + str(i + 1)] = {"I" + str(i + 1): 0,"E":0}
        else:
            probability["M"+str(i+1)] = {"I"+str(i+1):0,"M"+str(i+2):0,"D"+str(i+2):0}
            probability["D"+str(i+1)] = {"I"+str(i+1):0,"M"+str(i+2):0,"D"+str(i+2):0}

# print(probability)
# print(matrix)
for i in range(m):
    for j in range(n):
        if i==0 and matrix[j][i]!="-":
            probability["S"][matrix[j][i]]+=1
        elif i == 0 and matrix[j][i]=="-":
            probability["S"][matrix[j][i+1]]+=1
        elif i>0:
            if matrix[j][i]!="-":
                if matrix[j][i-1] != "-":
                    probability[matrix[j][i-1]][matrix[j][i]] +=1
                elif matrix[j][i-1] == "-"and matrix[j][i-2]!="-" and i>=2:
                    # print(i)
                    # print(j)
                    probability[matrix[j][i-2]][matrix[j][i]] +=1
                elif matrix[j][i-1] == "-" and matrix[j][i-2]=="-" and matrix[j][i-3]!="-":
                    probability[matrix[j][i-3]][matrix[j][i]] +=1
                elif matrix[j][i-1] == "-" and matrix[j][i-2]=="-"and matrix[j][i-3]=="-":
                    probability[matrix[j][i-4]][matrix[j][i]] +=1
for i in range(n):
    if matrix[i][m-1]!="-":
        probability[matrix[i][m-1]]["E"]+=1
    else:
        if matrix[i][m-2] != "-":
            probability[matrix[i][m-2]]["E"] +=1
        elif matrix[i][m-2] == "-"and matrix[i][m-3]!="-":
            probability[matrix[i][m-3]]["E"] +=1
        elif matrix[i][m-2] == "-" and matrix[i][m-3]=="-" and matrix[i][m-4]!="-":
            probability[matrix[i][m-4]]["E"] +=1
        elif matrix[i][m-2] == "-" and matrix[i][m-3]=="-"and matrix[i][m-4]=="-":
            probability[matrix[i][m-5]]["E"] +=1

# print(probability)
result = [[0 for i in range(3*(m-InsCount)+4)]for j in range(3*(m-InsCount)+4)]
result[0][0] = ""
result[0][1] = "S"
result[0][2] = "I0"
count = 0
for i in range(3,3*(m-InsCount)+3):
    # print(i)
    if i%3==0:
        count +=1
        result[0][i] = "M" + str(count)
        result[0][i+1] = "D"+str(count)
        result[0][i+2] = "I" + str(count)
result[0][3*(m-InsCount)+3] = "E"
result[1][0] = "S"
result[2][0] = "I0"
count = 0
for i in range(3,3*(m-InsCount)+3):
    # print(i)
    if i%3==0:
        count +=1
        result[i][0] = "M" + str(count)
        result[i+1][0] = "D"+str(count)
        result[i+2][0] = "I" + str(count)
result[3*(m-InsCount)+3][0] = "E"
# print(result)
sumNum = {}
for i in probability:
    sum = 0
    for j in probability[i]:
        sum += probability[i][j]
    sumNum[i] = sum
# print(sumNum)
# print(probability)





for i in probability:
    for j in probability[i]:
        if sumNum[i]!=0:
            probability[i][j] = probability[i][j]/sumNum[i]
# print(probability)

for i in probability:
    sum = 0
    for j in probability[i]:
        sum += probability[i][j]+sigma
    sumNum[i] = sum
# print(sumNum)
#
# probability2 = copy.deepcopy(probability)

for i in probability:
    for j in probability[i]:
        # if sumNum[i]!=0:
            probability[i][j] = (probability[i][j]+sigma)/(sumNum[i])
            # print(probability[i][j])


# print(probability)



for i in probability:
    for j in probability[i]:
        # if sumNum[i]!=0 and probability[i][j]!=0:

            # print(probability[i][j])
            result[result[0].index(i)][result[0].index(j)] = round(probability[i][j],3)





for i in range(len(result)):
    print(*result[i] , sep=" ")


print("--------")


result2 = [[0 for j in range(len(alphabet)+1)]for i in range(3*(m-InsCount)+4) ]
result2[0][0] = ""
result2[1][0] = "S"
result2[2][0] = "I0"
count = 0
for i in range(1,len(alphabet)+1):
    result2[0][i] = alphabet[i-1]
for i in range(3,3*(m-InsCount)+3):

    # print(i)
    if i%3==0:
        count +=1
        result2[i][0] = "M" + str(count)
        result2[i+1][0] = "D"+str(count)
        result2[i+2][0] = "I" + str(count)
result2[3*(m-InsCount)+3][0] = "E"
alphCount = {}
count = 0
for i in range(2):
    for j in range(len(alphabet)):
        if i ==0:
            if "S" in alphCount.keys():
                alphCount["S"].update({alphabet[j]:0})
            else:
                alphCount["S"] = {alphabet[j]:0}
        elif i ==1:
            if "I0" in alphCount.keys():
                alphCount["I0"].update({alphabet[j]:0})
            else:
                alphCount["I0"]={alphabet[j]:0}
for i in range((m-InsCount)):
    count+=1
    for j in range(len(alphabet)):

        if "M"+str(count) in alphCount.keys():
            alphCount["M"+str(count)].update({alphabet[j]:0})
        else:
            alphCount["M"+str(count)] = {alphabet[j]:0}
        if "D"+str(count) in alphCount.keys():
            alphCount["D"+str(count)].update({alphabet[j]:0})
        else:
            alphCount["D"+str(count)] = {alphabet[j]:0}
        if "I"+str(count) in alphCount.keys():
            alphCount["I"+str(count)].update({alphabet[j]:0})
        else:
            alphCount["I"+str(count)] = {alphabet[j]:0}

for j in range(len(alphabet)):
    if "E" in alphCount.keys():
        alphCount["E"].update({alphabet[j]:0})
    else:
        alphCount["E"] = {alphabet[j]:0}
for i in range(m):
    for j in range(n):
        if align[j][i]!="-":
            alphCount[matrix[j][i]][align[j][i]] += 1
# print(alphCount)
countalph = {}
for i in alphCount:
    sum = 0
    for j in alphCount[i]:
        sum += alphCount[i][j]
    countalph[i] = sum
# print(countalph)



for i in alphCount:
    for j in alphCount[i]:
        if countalph[i]!=0:
            alphCount[i][j] = alphCount[i][j]/countalph[i]
# print(alphCount)


for i in alphCount:
    sum = 0
    for j in alphCount[i]:
        sum += alphCount[i][j]
    countalph[i] = sum
# print(countalph)


for i in alphCount:
    for j in alphCount[i]:
        # if i[0]=="I":
            alphCount[i][j] = (alphCount[i][j]+sigma)/(countalph[i]+len(alphabet)*sigma)
        # if i[0]=="I" and countalph[i] == 0:
        #     # print(i)
        #     alphCount[i][j] = 1/ (len(alphabet))

# print(alphCount)








count = 0
# print(result2[15][0])
for i in (alphCount):
    count+=1
    # print(count)
    for j in (alphCount[i]):
        # print(j)
        if (alphCount[i][j]!=0 and countalph[i]!=0) or i[0]=="I":
            result2[count][result2[0].index(j)] = round(alphCount[i][j],3)
for i in range(len(result2)):
    print(*result2[i] , sep=" ")
