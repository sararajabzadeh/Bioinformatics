import copy
i = input()
array = []
while i!="*":
    array += [i.split(" -> ")]
    i = input()
# print(array)
inp = {}
ex = {}
chars = {}
for i in range(len(array)):
    for j in range(len(array[i])):
        if len(array[i][1]) ==1:
            chars[array[i][0]] = "*"
            chars[array[i][1]]= "*"
        elif len(array[i][1]) >1:
            temp = array[i][1].split(",")
            chars[array[i][0]] = "*"
            for k in range(len(temp)):
                chars[temp[k]] = "*"

for i in chars:
    inp[i] = []
    ex[i] = []

for i in range(len(array)):
        if len(array[i][1]) ==1:
            ex[array[i][0]] += array[i][1]
            inp[array[i][1]] += [array[i][0]]
        elif len(array[i][1]) >1:
            temp = array[i][1].split(",")
            ex[array[i][0]] += temp
            for k in range(len(temp)):
                inp[temp[k]] += [array[i][0]]



# print(chars)
# print(inp)
# print(ex)
path = []
nonBranchingPath = []
visit = copy.deepcopy(chars)
for i in chars:
    visit[i] = False
# print(visit)
for i in chars:
    # print("i")
    # print(i)
    if len(ex[i])!=1 or len(inp[i])!=1:
        if len(ex[i]) > 0:
            for j in ex[i]:
                nonBranchingPath = []
                # print("j")
                # print(j)
                nonBranchingPath += [i]
                nonBranchingPath += [j]
                visit[i] = True
                visit[j] = True
                # print("ex[j]")
                # print(ex[j])
                # print("nonBranch")
                # print(nonBranchingPath)
                while len(ex[j])==1 and len(inp[j])==1:
                    nonBranchingPath +=ex[j]
                    # print("nonBranch")
                    # print(nonBranchingPath)
                    # print("ex")
                    # print(ex[j][0])
                    visit[ex[j][0]] = True
                    # print("visit")
                    # print(visit)
                    j = ex[j][0]
                    # print("j")
                    # print(j)
                path += [nonBranchingPath]
                # print("Path")
                # print(path)
# print(visit)
for i in chars:
    if visit[i]==False:
        nonBranchingPath = []

        while len(ex[i])==1 and len(inp[i])==1 and visit[i]==False:
                nonBranchingPath += [i]
                # nonBranchingPath += [ex[i]]
                visit[i] = True
                # visit[ex[i]] = True
                i = ex[i][0]
        # print(nonBranchingPath[0])
        nonBranchingPath += [nonBranchingPath[0]]
        path += [nonBranchingPath]

# print(path)
for i in range(len(path)):
    print(' -> '.join(path[i]))



