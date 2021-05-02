def PatternCount(pattern , text):
    count =0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)]==pattern:
            count+=1

    return count

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

genome = input()
symbol = input()
SymbolArray(genome , symbol)