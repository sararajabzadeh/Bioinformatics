k = int(input())
text = input()
dic = {}
# print(len(text))
for i in range(len(text)-k+1):
    # print(text[i:i+k-1])
    # print(text[i+1:i+k])
    if text[i:i+k-1] in dic.keys():
        dic[text[i:i+k-1]] += [text[i+1:i+k]]
    else:
        dic[text[i:i + k - 1]] = [text[i + 1:i + k]]
# print(dic)
# for i in dic:
#     dic[i].sort()
array = []
for i in dic:
    array+=[i]
    array+= [" -> "]
    array+= [dic[i]]
# print(array)
temp = []
# print(len(array)-k+2)
for i in range(len(array)):
    # print(i)
    if i%3==0:
        # print("hello")
        temp += [array[i]+array[i+1]+ ','.join(array[i+2])]
# print(temp)
# temp.sort()
for i in range(len(temp)):
    print(temp[i])