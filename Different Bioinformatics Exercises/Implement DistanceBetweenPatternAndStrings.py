import math
def hamming(in1 , in2):
    count = 0
    for i in range(len(in1)):
        if in1[i]!= in2[i]:
            count += 1
    return count

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for i in Dna:
        hammingDist = math.inf
        for j in range(len(i)-len(Pattern)+1):
            patt = i[j:j+k]
            if hammingDist>hamming(patt , Pattern):
                hammingDist = hamming(patt , Pattern)
        distance += hammingDist
    return distance

pattern = input()
Dna = []
Dna += map(str , input().split())
print(DistanceBetweenPatternAndStrings(pattern , Dna))