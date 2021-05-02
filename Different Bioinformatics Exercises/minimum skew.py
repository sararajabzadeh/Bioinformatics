def MinimumSkew(Genome):
    positions = []
    skew = SkewArray(Genome)
    for key in skew:
        if skew[key]==min(skew.values()):
            positions +=[key]

    return positions


def SkewArray(Genome):

    array ={0:0}
    for i in range(1,len(Genome)+1):
        if Genome[i-1]=="A" or Genome[i-1]=="T":
            array[i] = array[i-1]
        elif Genome[i-1]=="C":
            array[i] = array[i-1]-1
        elif Genome[i-1]=="G":
            array[i] = array[i-1]+1
    return array
Genome = input()
print(*MinimumSkew(Genome) , sep=" ")