DNA = input()
pattern = input()
array = []
for i in range(len(DNA)):
    if DNA[i:i+len(pattern)] == pattern:
        array += [i+1]
print(*array , sep=" ")