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


def Frequencies(text , k):
    string = []
    frequency = [0]*(4**k)
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        # pattern1 = "".join(ReverseComplement(text[i:i+k]))
        temp1 = patternToNumber(pattern)
        # temp2 = patternToNumber(pattern1)
        frequency[temp1] += 1

    return frequency

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

def ClumpFinding(Genome, k, L, t):
    freqPattern = []
    clump = [0]*(4**k)
    for i in range(len(Genome)-k+1):
        text = Genome[i:i+L]
        freqArray = Frequencies(text , k)
        for i in range(4**k):
            if freqArray[i] >= t:
                clump[i] = 1
    for i in range(4**k):
        if clump[i] == 1:
            pattern = NumberToPattern(i , k)
            freqPattern+=[pattern]
    return freqPattern

genome = input()
k , L , t = map(int , input().split())
temp = ClumpFinding(genome , k , L , t)
array = []
for i in range(len(temp)):
    array += ["".join(reversed(temp[i]))]
print(*array , sep=" ")