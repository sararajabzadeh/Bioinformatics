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
# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
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

Motifs = ["CCA","CCT","CTT","TTG"]
print(Profile(Motifs))