def PatternCount(Text , Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count+=1
    return count

def FrequentWords(Text , k):
    FrequentPatterns = {}
    temp = []
    count = [0]*(len(Text)-k+1)
    for i in range(len(Text) - k +1):
        Pattern = Text[i:i+k]
        count[i] = PatternCount(Text , Pattern)
    maxCount = max(count)
    for i in range(len(Text)-k+1):
        if count[i]==maxCount:
            FrequentPatterns[Text[i:i+k]] = 1
    for i in FrequentPatterns.keys():
        temp += [i]
    return temp

Text = input()
k = int(input())
print(*FrequentWords(Text,k), sep=" ")