import random
#
# def Count(Motifs):
#     count = {}
#     k = len(Motifs[0])
#     for symbol in "ACGT":
#         count[symbol] = []
#         for j in range(k):
#              count[symbol].append(0)
#     t = len(Motifs)
#     for i in range(t):
#         for j in range(k):
#             symbol = Motifs[i][j]
#             count[symbol][j] += 1
#     return count
def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    profile = {}
    count = CountWithPseudocounts(Motifs)
    #print(count)
    for i in "ACTG":
        for j in range(k):
            #symbol = Motifs[i][j]
            count[i][j]= count[i][j]/t
    return count

def Consensus(Motifs):
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Score(Motifs):
    count = 0
    k = len(Motifs[0])
    t = len(Motifs)
    word = Consensus(Motifs)
    for i in range(t):
        for j in range(k):
            if Motifs[i][j]!=word[j]:
                count+=1
    return count

def Pr(Text, Profile):
    result = 1
    # print(Text)
    for i in range(len(Text)):
        # print(i)
        result *= Profile[Text[i]][i]
    return result


def ProfileMostProbableKmer(text, k, profile):
    prob = []
    # print(text[1:3+1])
    #result = 0
    for i in range(len(text)-k+1):
        # print(i)
        # print(text[i:i+k])
        prob += [Pr(text[i:i+k] , profile)]
    for i in range(len(prob)):
        if prob[i]==max(prob):
            #result = text[i:i+k]
            return text[i:i+k]

def Motifs(Profile, Dna,k):
    motifs = []
    t = len(Dna)
    # k = len(Dna[0])
    for i in range(t):
        # print(Dna[i])
        motif = ProfileMostProbableKmer(Dna[i], k, Profile)
        motifs.append(motif)
    return motifs




# def Profile(Motifs):
#     t = len(Motifs)
#     k = len(Motifs[0])
#     #print(k)
#     profile = {}
#     count = Count(Motifs)
#     #print(count)
#     for i in "ACTG":
#         for j in range(k):
#             #symbol = Motifs[i][j]
#             count[i][j]= count[i][j]/t
#     return count

def RandomMotifs(Dna, k, t):
    # l = len(Dna[0])
    RandomMotifs = []
    for i in range(t):
        rand = random.randint(0, len(Dna[0])-k)
        # print("rand")
        # print(rand)
        RandomMotifs.append(Dna[i][rand:rand+k])
    # print(RandomMotifs)
    return RandomMotifs

def RandomizedMotifSearch(Dna, k, t):
    Mot = RandomMotifs(Dna, k, t)
    BestMotifs = Mot
    while True:
        profile = ProfileWithPseudocounts(Mot)
        # print(profile)
        Mot = Motifs(profile, Dna , k)
        if Score(Mot) < Score(BestMotifs):
            BestMotifs = Mot
        else:
            return BestMotifs

k , t = map(int,input().split())
DNA = []
N=1000
for i in range(t):
    DNA+=[input()]
# print(DNA)
# M=""
# print(RandomizedMotifSearch(DNA,k,t))
RandomizedMotifSearch(DNA, k, t)
Mot = RandomizedMotifSearch(DNA, k, t)
BestMotifs = Mot

for i in range(N+1):
    Mot = RandomizedMotifSearch(DNA, k, t)
    if Score(Mot) < Score(BestMotifs):
         BestMotifs = Mot
    else:
        bestMotifs = BestMotifs
for i in range(len(bestMotifs)):
    print(*bestMotifs[i],sep="")