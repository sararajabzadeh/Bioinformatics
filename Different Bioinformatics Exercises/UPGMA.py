import math

def getMinValue(v):
    minVal = float('inf')
    length = len(v)
    for i in range(length):
        for j in range(length):
            if v[i][j] < minVal and v[i][j] != 0:
                minVal = v[i][j]
                pos = [i,j]
    return minVal, pos


def UPGMA(D , n):
    clusters = []
    tree = []
    for i in range(n):
        tree += [i]
    T={}
    for i in range(n):
        T[i] = "-"
    # print(T)
    for i in range(n):
        clusters += [i]
    # print(clusters)
    age = [0]*(n)
    result = []
    vec = []
    codID = ord('A')
    length = len(D)
    for i in range(length):
        vec.append(chr(codID))
        codID += 1

    counter1 = n
    while len(D)>1:
        counter = 0
        # counter1= n
        value, pos = getMinValue(D)
        # print(value, pos)
        newCluster = len(T)+counter
        # print(pos)
        # T[len(T)+counter] = pos
        # print(T)
        # print("cluster")
        # print(clusters)
        for i in range(len(pos)):
            # print("counter1")
            # print(counter1)
            if counter1 in T.keys():
                T[counter1] += [clusters[pos[i]]]
                # print("T[counter1]")
                # print(T[counter1])
            else:
                T[counter1] = [clusters[pos[i]]]
        counter1 +=1
        # print(T)

        age += [D[pos[0]][pos[1]]/2]

        # print(age)

        count0 = len(vec[pos[0]])
        count1 = len(vec[pos[1]])
        for i in range(length):
            if i != pos[0]:
                D[i][pos[0]] = ((D[i][pos[0]] * count0) + (D[i][pos[1]] * count1)) / (count0 + count1)
                # print(D[i][pos[0]])
                D[pos[0]][i] = D[i][pos[0]]
        D.pop(pos[1])
        for coluna in D:
            coluna.pop(pos[1])
        result.append((vec[pos[0]], vec[pos[1]]))
        vec[pos[0]] += vec[pos[1]]
        vec.pop(pos[1])

        # pos.sort(reverse=True)
        # for i in range(len(pos)):
        #     clusters.pop(pos[i])
            # print(clusters)
        clusters[pos[0]] = newCluster
        clusters.pop(pos[1])
        # print(clusters)
        counter+=1
        # print("---------------------------------------------------------")
        result = []
        length -= 1
        # print(T)
        # print(age)
    for i in range(len(T)):
        if T[i] != "-":
            for j in range(len(T[i])):
                # print(len(T[i]))
                # print(i)
                # print(j)
                if T[T[i][j]] =="-":
                    T[T[i][j]] = [i]
                    # print("HHHh")
                else:
                    # print("TTTT")
                    T[T[i][j]] += [i]
                # print(T)
    # print("T")
    # print(T)
    # print(age)
    for i in range(len(T)):
        for j in T[i]:
            # print(i)
            # print(j)
            matrix = "{:.3f}".format(abs(age[i]-age[j]))
            print(str(i)+"->"+str(j)+":"+str(matrix))
    return


matrix = []
n = int(input())
for i in range(n):
    matrix+=[input().split("\t")]
# print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] = int(matrix[i][j])
print(matrix)
# matrix=[[0,20,17,11],
#         [20,0,20,13],
#         [17,20,0,10],
#         [11,13,10,0]]
# matrix=[[0,3,4,3],
#         [3,0,4,5],
#         [4,4,0,2],
#         [3,5,2,0]]


# matrix=[[0,17,21,31,23],
#         [17,0,30,34,21],
#         [21,30,0,28,39],
#         [31,34,28,0,43],
#         [23,21,39,43,0]]
# n=4

UPGMA(matrix,n)