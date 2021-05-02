# Insert your completed FrequencyMap() function here.
def FrequencyMap(Text, k):
    freq ={}
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        freq[pattern] = 0
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        freq[pattern] +=1
    print(freq)
    return freq

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        print(freq[key])
        if freq[key] == m:
            words += [key]
        print(key)
        print(freq[key])
        print(words)

    return words

text = input()
k = int(input())
print(FrequentWords(text , k))