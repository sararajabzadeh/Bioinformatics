
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
def Motifs(Profile, Dna):
    motifs = []
    t = len(Dna)
    k = 3
    for i in range(t):
        motif = ProfileMostProbableKmer(Dna[i], k, Profile)
        motifs.append(motif)
    return motifs

profile = {'A': [0.0, 0.0, 0.25], 'C': [0.75, 0.5, 0.0], 'G': [0.0, 0.0, 0.25], 'T': [0.25, 0.5, 0.5]}
Dna = ["AAGCCAAA","AATCCTGG","GCTACTTG","ATGTTTTG"]
print(Motifs(profile , Dna))