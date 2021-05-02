import copy
def getMinValue(v):
    minVal = float('inf')
    length = len(v)
    for i in range(length):
        for j in range(length):
            if v[i][j] < minVal and v[i][j] != 0:
                minVal = v[i][j]
                position = [i,j]
    return position

def NeighborJoining(D,n,n1,clusters):
    if n ==2:
        edge={}
        edge[clusters[0]] = [clusters[1]]
        edge[clusters[1]] = [clusters[0]]
        weight = {}
        weight[(clusters[0],clusters[1])] = D[0][1]
        weight[(clusters[1],clusters[0])] = D[0][1]
        # print(T)
        # print(n1)
        # print(edge)
        # print(weight)
        return (edge,weight,n1)
    # clusters = []

    # T = {}
    # for i in range(n):
    #     T[i] = "-"
    # print(T)
    # for i in range(n):
    #     clusters += [i]
    # print(clusters)
    DPrime = [[0 for i in range(n)] for j in range(n)]
    # print(D[0][1])
    for i in range(n):
        for j in range(n):
            if i != j:
                DPrime[i][j] = (n-2)*D[i][j] - sum(D[i][:]) - sum(D[:][j])
    # print(DPrime)
    position = getMinValue(DPrime)
    Delta = (sum(D[position[0]][:]) - sum(D[:][position[1]]))/(n-2)
    limbLengthI = (D[position[0]][position[1]] + Delta)/2
    limbLengthJ = (D[position[0]][position[1]] - Delta)/2
    Limb = [0]*n
    temp = [0]*(len(D))
    for i in range(n):
        temp[i] = (D[i][position[0]]+D[i][position[1]] - D[position[0]][position[1]])/2
         # = D[position[0]][i]

    # print(temp)
    D[position[0]] = temp
    for i in range(len(D)):
        D[i][position[0]] = temp[i]
    # print(D)
    # print(position)
    for i in range(n):
        D[i].pop(position[1])
    # for i in range(n-1):
    #     D[position[1]].pop(i)
    D.pop(position[1])
    # print(D)

    # clusters[position[0]] = n1
    # print(clusters)
    # clusters.pop(position[1])
    # print(clusters)
    # Temp=[]
    clustersPrime = copy.deepcopy(clusters)
    clustersPrime[position[0]] = n1
    clustersPrime.pop(position[1])
    n1 += 1
    edge, weight, n2= NeighborJoining(D,n-1,n1,clustersPrime)
    if clusters[position[0]] not in edge:
        edge[clusters[position[0]]]=[]
    if clusters[position[1]] not in edge:
        edge[clusters[position[1]]]=[]
    if n1-1 not in edge:
        edge[n1-1]=[]
    edge[clusters[position[0]]].append(n1-1)
    edge[clusters[position[1]]].append(n1 -1)
    edge[n1-1].append(clusters[position[0]])
    edge[n1-1].append(clusters[position[1]])
    weight[(clusters[position[0]],n1-1)]=weight[(n1-1,clusters[position[0]])]= limbLengthI
    weight[(clusters[position[1]],n1-1)]=weight[(n1-1 ,clusters[position[1]])] =limbLengthJ
    # print(edge)
    # print(weight)

    return edge,weight,n2
    # print(T)
    # print(Limb)

# matrix=[[0,20,17,11],
#         [20,0,20,13],
#         [17,20,0,10],
#         [11,13,10,0]]
# matrix=[[0,3,4,3],
#         [3,0,4,5],
#         [4,4,0,2],
#         [3,5,2,0]]
# matrix = [[0,13,21,22],
#           [13,0,12,13],
#           [21,12,0,13],
#           [22,13,13,0]]

matrix = []
n = int(input())
for i in range(n):
    matrix+=[input().split()]
# print(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] = int(matrix[i][j])
# print(matrix)
# matrix=[[0,17,21,31,23],
#         [17,0,30,34,21],
#         [21,30,0,28,39],
#         [31,34,28,0,43],
#         [23,21,39,43,0]]
# n=4
clusters = []
for i in range(n):
    clusters += [i]
edge , weight , t =NeighborJoining(matrix,n,n,clusters)
for i in sorted(edge):
    for j in (edge[i]):
        print(str(i) + "->" + str(j) + ":" + str("{:.3f}".format(round(weight[(i, j)], 3))))