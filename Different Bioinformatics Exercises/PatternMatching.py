def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions += [i]
    return positions
pattern = input()
Genome = input()
print(PatternMatching(pattern , Genome))