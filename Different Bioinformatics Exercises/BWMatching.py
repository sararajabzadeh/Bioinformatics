import copy
def BWMatching(firstColumn , lastColumn , pattern , lastToFirst):
    top = 0
    bottom = len(lastColumn)-1
    topIndex=0
    bottomIndex =0
    temp = 1
    while top<=bottom:
        if temp<=len(pattern):
            symbol = pattern[len(pattern)-temp]
            # print(symbol)
        # pattern.pop(len(pattern)-1)
            counter = 0
            if symbol in lastColumn[top:bottom+1]:
                for i in range(top,bottom+1):
                    if symbol == lastColumn[i]:
                        counter+=1
                        if counter==1:
                            topIndex = i
                            break
                counter=0
                for i in range(bottom,top-1,-1):
                    if symbol==lastColumn[i]:
                        counter+=1
                        if counter==1:
                            bottomIndex = i
                            break
            else:return 0
            top = lastToFirst[topIndex]
            bottom = lastToFirst[bottomIndex]
            temp+=1
            # print(top)
            # print(bottom)
        else:
            return bottom-top+1

string = input()
temp = input()
array = []
array+= temp.split(" ")
lastColumn = []
for i in range(len(string)):
    lastColumn += [string[i]]
# print(lastColumn)
firstColumn = copy.deepcopy(lastColumn)
firstColumn.sort()
firstColumn = "".join(firstColumn)
# print(firstColumn)
lastToFirst = []
result = []
dic = {}
dic2= {}

for i in range(len(firstColumn)):
    if firstColumn[i] in dic.keys():
        dic[firstColumn[i]]+=1
    else:
        dic[firstColumn[i]]=1
        dic2[firstColumn[i]] = 0
# print(dic)
# print(lastColumn)
# print(firstColumn)
for i in range(len(lastColumn)):
    counter = 1
    dic2[lastColumn[i]]+=1
    for j in range(len(firstColumn)):
        if firstColumn[j]==lastColumn[i] and counter==dic2[lastColumn[i]]:
            lastToFirst += [j]
            break
        elif firstColumn[j]==lastColumn[i] and counter!=dic2[lastColumn[i]]:
            counter+=1
        # print(i)
        # print(j)
        # print(dic2)
        # print("last")
        # print(lastToFirst)
for i in array:
    result += [BWMatching(firstColumn , lastColumn,i,lastToFirst)]
# print(lastToFirst)
print(*result,sep=" ")