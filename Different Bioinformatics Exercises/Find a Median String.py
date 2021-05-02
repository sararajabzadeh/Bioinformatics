import math
def hamming(pattern,pattern2):
    count = 0
    for i in range(len(pattern)):
        if pattern[i]!= pattern2[i]:
            count += 1
    return count

def Distance(pattern , DNA):
    k = len(pattern)
    distance = 0
    for i in range(len(DNA)):
        HammingDistance = math.inf
        for j in range(len(DNA[0])-k+1):
            # print(DNA[i][j:j+k])
            if HammingDistance>hamming(pattern,DNA[i][j:j+k]):
                HammingDistance = hamming(pattern,DNA[i][j:j+k])
                # print(HammingDistance)
        distance+=HammingDistance
    return distance

k = int(input())
temp = input()
Dna = []
while temp!=".":
    Dna+=[temp]
    temp = input()
# print(Dna)
PatternList = []
for i in range(len(Dna)):
    for j in range(len(Dna[0])-k+1):
        PatternList += [Dna[i][j:j+k]]
# print(PatternList)
distance = {}
for i in range(len(PatternList)):
    # print(PatternList[i])
    distance[PatternList[i]] = Distance(PatternList[i],Dna)
# print(distance)
    # print(Distance(PatternList[i],Dna))
distancemin = math.inf
result =""
for i in distance.keys():
    # print(i)
    if distancemin > distance[i]:
        distancemin=distance[i]
        result = i
print(result)