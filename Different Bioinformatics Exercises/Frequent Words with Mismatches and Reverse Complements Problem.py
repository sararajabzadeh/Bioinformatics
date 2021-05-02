def ReverseComplement(text):
    str = []

    for i in range(len(text) - 1, -1, -1):
        if (text[i] == "A"):
            str += ["T"]
        elif (text[i] == "T"):
            str += ["A"]
        elif (text[i] == "C"):
            str += ["G"]
        elif (text[i] == "G"):
            str += ["C"]
    return str



def symbolToNumber(symbol):
    if symbol=="A":
        return 0
    elif symbol=="C":
        return 1
    elif symbol =="G":
        return 2
    elif symbol=="T":
        return 3

def patternToNumber(pattern):

    if pattern =="":
        return 0
    count = 0
    symbol = pattern[len(pattern)-1]
    prefix = pattern[:len(pattern)-1]
    # print(prefix)
    count += 4*patternToNumber(prefix)+symbolToNumber(symbol)
    # print(count)
    return count

def NumberToSymbol(num):
    if num == 0:
        return "A"
    elif num == 1:
        return "C"
    elif num == 2:
        return "G"
    elif num == 3:
        return "T"

def NumberToPattern(index , k):
    array = []
    if k==1:
        return NumberToSymbol(index)
    prefixIndex = index//4
    r = index%4
    symbol = NumberToSymbol(r)
    prefixPattern = NumberToPattern(prefixIndex , k-1)
    array+=[symbol]
    array+=prefixPattern
    return array

def neighbors(pattern, d):
    if d <=0 :
        return [pattern]
    neighbor = []
    suffix = neighbors(pattern[1:] , d-1)

    for i in suffix:
        for j in "ACGT":
            if j!=pattern[0]:
                neighbor += [j+i]


    if d<len(pattern):
        suffix = neighbors(pattern[1:] , d)
        for i in suffix:
            neighbor += [pattern[0]+i]
    return neighbor

def Frequencies(text , k , d):
    string = []
    frequency = [0]*(4**k)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        pattern1 = "".join(ReverseComplement(text[i:i+k]))
        temp1 = patternToNumber(pattern)
        temp2 = patternToNumber(pattern1)
        frequency[temp1] += 1
        frequency[temp2] += 1
        neighborhood = neighbors(pattern,d)
        neighborhood1 = neighbors(pattern1 , d)
        for j in neighborhood:
            temp = patternToNumber(j)
            frequency[temp] += 1
        for l in neighborhood1:
            temp3 = patternToNumber(l)
            frequency[temp3] += 1

    for i in range(len(frequency)):
        if frequency[i] == max(frequency):
            string += [NumberToPattern(i , k)]
    return string


text = input()
k , d = map(int , input().split())
temp =Frequencies(text , k , d)

res = []
for i in range(len(temp)):
    res += ["".join(reversed(temp[i]))]

print(*res , sep=" ")