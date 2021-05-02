def Clump(genome , k ,L,t):
    result = []
    for i in range(len(genome)-L+1):
        text = genome[i:i+L]
        frequency = {}
        for j in range(len(text)-k+1):
            if text[j:j+k] not in frequency.keys():
                frequency[text[i:i+k]] = 1
            else:
                frequency[text[i:i+k]] +=1
        for l in frequency:
            if frequency[l]>=t and l not in result:
                result.append(l)
    return result
# file = open("/Users/sara/Downloads/dataset_206123_5.txt")
# genome = file.read()
genome = input()
k , l , t = map(int,input().split())
result = Clump(genome,k,l,t)
print(result)
# print(len(result))