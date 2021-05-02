def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count

def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
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

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    #print(k)
    profile = {}
    count = Count(Motifs)
    #print(count)
    for i in "ACTG":
        for j in range(k):
            #symbol = Motifs[i][j]
            count[i][j]= count[i][j]/t
    return count
# Then copy your ProfileMostProbableKmer(Text, k, Profile) and Pr(Text, Profile) functions here.
def Pr(Text, Profile):
    result = 1
    for i in range(len(Text)):
        result *= Profile[Text[i]][i]
    return result


def ProfileMostProbableKmer(text, k, profile):
    prob = []
    #result = 0
    for i in range(len(text)-k+1):
        prob += [Pr(text[i:i+k] , profile)]
    for i in range(len(prob)):
        if prob[i]==max(prob):
            #result = text[i:i+k]
            return text[i:i+k]
# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = Profile(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


k , d = map(int , input().split())

Dna = []
while True:
    i = 0
    temp = input()
    if temp == ".":
        break
    else:
        Dna += [temp]
        print(GreedyMotifSearch(Dna , k , d))
    i += 1

print(Dna[1][1])
