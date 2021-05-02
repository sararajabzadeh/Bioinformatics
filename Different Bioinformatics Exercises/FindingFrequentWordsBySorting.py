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

def FindingFrequentWordsBySorting(Text , k):
    freqPattern = []
    index = [0]*(len(Text) - k +1)
    count = [0] * (len(Text) - k +1)
    for i in range(len(Text) - k +1):
        pattern = Text[i:i+k]
        index[i] = patternToNumber(pattern)
        count[i] +=1
    index.sort()
    for i in range(1,len(Text)-k+1):
        if index[i] == index[i-1]:
            count[i] = count[i-1]+1
    for i in range(1,len(Text)-k+1):
        if count[i] == max(count):
            pattern = NumberToPattern(index[i] , k)
            freqPattern += [pattern]
    return freqPattern

text = input()
k = int(input())
temp = FindingFrequentWordsBySorting(text , k)
array = []
for i in range(len(temp)):
    array += ["".join(reversed(temp[i]))]
print(*array , sep=" ")