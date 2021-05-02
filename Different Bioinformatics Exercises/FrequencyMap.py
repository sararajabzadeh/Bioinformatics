# Insert your completed FrequencyMap() function here.
def FrequencyMap(Text, k):
    freq ={}
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        freq[pattern] = 0
    for i in range(len(Text)-k+1):
        pattern = Text[i:i+k]
        freq[pattern] +=1
    return freq

k = int(input())
Text = input()
print(FrequencyMap(Text , k))