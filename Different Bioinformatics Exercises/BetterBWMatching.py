def BetterBWMatching(FirstOccurrence, LastColumn, Pattern, Count):
    top = 0
    bottom = len(LastColumn) - 1

    while top <= bottom:
        if len(Pattern)>=1:
            symbol = Pattern[len(Pattern)-1]
            Pattern = Pattern[:len(Pattern)-1]
            # Pattern = Pattern[len(Pattern)-temp]
            if symbol in LastColumn[top:bottom+1]:
                top = FirstOccurrence[symbol] + Count[symbol][top]
                bottom = FirstOccurrence[symbol] + Count[symbol][bottom+1] - 1
                # print(top)
                # print(bottom)
                # print("hello")
            else:
                # print("0")
                return 0

        else:
            # print(bottom-top+1)
            return bottom - top + 1

string = input()
temp = []
for i in range(len(string)):
    temp += string[i]
temp.sort()

array = input().split(" ")
LastColumn = []
for i in range(len(string)):
    LastColumn += [string[i]]

FirstOccurence = {}
Count = {"A":[0],"C":[0],"G":[0],"T":[0] ,"$":[0]}
# Count = [[0]for i in range(5)]
for i in range(len(temp)-1,-1,-1):
    FirstOccurence[temp[i]] = i
for i in range(len(string)):
    if string[i] == "A":
        Count["A"] += [max(Count["A"])+1]
        Count["C"] += [max(Count["C"])]
        Count["G"] += [max(Count["G"])]
        Count["T"] += [max(Count["T"])]
        Count["$"] += [max(Count["$"])]
    elif string[i] == "C":
        Count["C"] += [max(Count["C"])+1]
        Count["A"] += [max(Count["A"])]
        Count["G"] += [max(Count["G"])]
        Count["T"] += [max(Count["T"])]
        Count["$"] += [max(Count["$"])]
    elif string[i] == "G":
        Count["G"] += [max(Count["G"])+1]
        Count["A"] += [max(Count["A"])]
        Count["C"] += [max(Count["C"])]
        Count["T"] += [max(Count["T"])]
        Count["$"] += [max(Count["$"])]
    elif string[i] == "T":
        Count["T"] += [max(Count["T"])+1]
        Count["A"] += [max(Count["A"])]
        Count["C"] += [max(Count["C"])]
        Count["G"] += [max(Count["G"])]
        Count["$"] += [max(Count["$"])]
    elif string[i] == "$":
        Count["$"] += [max(Count["$"])+1]
        Count["A"] += [max(Count["A"])]
        Count["C"] += [max(Count["C"])]
        Count["G"] += [max(Count["G"])]
        Count["T"] += [max(Count["T"])]

print(FirstOccurence)
print(Count)
print(array)
result = []
for i in range(len(array)):
    result.append(BetterBWMatching(FirstOccurence,LastColumn,array[i] , Count))
print(*result,sep=" ")
