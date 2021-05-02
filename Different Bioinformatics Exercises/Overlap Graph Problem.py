def Prefix(string):
    return string[0:len(string)-1]
def Sufix(string):
    return string[1:len(string)]

array = []
t = ""
dic = {}
while t!="*":
    t = input()
    array +=[t]
array.remove(array[len(array)-1])
matrix = [[0 for x in range(len(array))] for y in range(len(array))]
for i in range(len(array)):
    for k in range(len(array)):
        if Sufix(array[i])==Prefix(array[k]):
            dic[array[i]] = array[k]
for i in dic:
    print(i+" -> "+dic[i])
