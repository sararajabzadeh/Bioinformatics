def SkewArray(Genome):
    array =[0]
    for i in range(len(Genome)):
        if Genome[i]=="A" or Genome[i]=="T":
            array += [array[i]]
        elif Genome[i]=="C":
            array += [array[i]-1]
        elif Genome[i]=="G":
            array += [array[i]+1]
    return array

Genome = input()
print(SkewArray(Genome))