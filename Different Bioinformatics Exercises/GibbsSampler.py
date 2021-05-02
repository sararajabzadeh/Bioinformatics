import random , math , copy
def RandomMotifs(Dna, k, t):
    l = len(Dna[0])
    RandomMotifs = []
    for i in range(t):
        rand = random.randint(1,l-k)
        RandomMotifs.append(Dna[i][rand:rand+k])
    return RandomMotifs

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

    count = CountWithPseudocounts(Motifs)
    #print(count)
    for i in "ACTG":
        for j in range(k):
            #symbol = Motifs[i][j]
            count[i][j]= count[i][j]/t
    return count

def WeightedDie(Probabilities):
    ran = random.uniform(0,1)
    # print(Probabilities)
    for i in Probabilities:
        ran -= Probabilities[i]
        if ran <0:
            return i

def Normalize(Probabilities):
    normalized={}
    for j in Probabilities:
        normalized[j] = Probabilities[j]/sum(Probabilities.values())
    return normalized

def Pr(Text, Profile):
    p = 1
    for i in range(0,len(Text)):
        p *= Profile[Text[i]][i]
    return p

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)


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

def GibbsSampler(Dna, k, t, N):
    Motif = RandomMotifs(Dna , k , t)
    BestMotifs = Motif
    # minscore = math.inf
    for j in range(1 , N+1):
        i = random.randrange(t)
        del Motif[i]
        profile = ProfileWithPseudocounts(Motif)
        # print(profile)
        Motif.insert(i , ProfileGeneratedString(Dna[i] , profile,k))
        # print(Motif)
        if Score(Motif)<Score(BestMotifs):
            BestMotifs = Motif
            
    return BestMotifs

k , t , N= map(int,input().split())
DNA = []
for i in range(t):
    DNA += [input()]

GibbsSampler(DNA,k,t,N)
gibbs  = GibbsSampler(DNA,k,t,N)
BestMotifs = gibbs
for i in range(21):
    gibbs = GibbsSampler(DNA,k,t,N)
    if Score(gibbs) < Score(BestMotifs):
        BestMotifs = gibbs
for i in range(len(BestMotifs)):
    print(*BestMotifs[i],sep="")