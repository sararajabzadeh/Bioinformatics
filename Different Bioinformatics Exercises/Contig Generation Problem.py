i = input()
array = []
while i != "*":
    array += [i]
    i = input()
n = len(array[0])
dic = {}
dic2={}
for i in range(len(array)):
    if array[i][:n-1] not in dic:
        dic[array[i][:n-1]] = []
    if array[i][1:n] not in dic:
        dic[array[i][1:n]] =[]

for i in range(len(array)):
    # if array[i][:n-1] in dic.keys():
        dic[array[i][:n-1]] += [array[i][1:n]]
    # else:
    #     dic[array[i][:n-1]] = [array[i][1:n]]
# print(dic)

for i in dic:
    for j in range(len(array)):
        if array[j][1:n] == i:
            if i in dic2.keys():
                dic2[i]+=[array[j][:n-1]]
            else:
                dic2[i] = [array[j][:n-1]]
    if i not in dic2.keys():
        dic2[i] =[]
# print(dic2)
result=[]
string=""
for i in dic.keys():
    if dic[i]!=[]:
        if len(dic[i]) != 1 or len(dic2[i]) != 1:
            # print("Y")
            for j in dic[i]:
                string=i
                string=string+j[-1]
                # print(string)
                if dic[j]!=[]:
                    if len(dic[j])!= 1 or len(dic2[j])!=1:
                        result+=[string]
                        continue
                    else:
                        k=dic[j][0]
                        string=string+k[-1]
                        # print(string)
                        while (dic[k]!=[] and (len(dic[k])==1) and (len(dic2[k])==1)):
                            k=dic[k][0]
                            string=string+k[-1]
                        result+=[string]
                else:
                    result+=[string]
                    # print(result)
                    continue
print(*result,sep=" ")