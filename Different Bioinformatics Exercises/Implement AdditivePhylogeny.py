import numpy as np
import math

def LimbLength(matrix, j):
    array = []
    limb = math.inf
    for i in range(matrix.shape[0]):
        if i != j:
            array += [i]
    # print(array)

    for k in range(matrix.shape[0]):
        if k != j:
            limb = min(limb, min(matrix[array, j]+ matrix[j, k] - matrix[array, k] ))
            # print(limb)
    return limb // 2


def FindingIAndK(matrix):

    for i in range(matrix.shape[0] - 1):
        array = matrix[i] - matrix[-1]
        # print(array)
        index = np.where(array == matrix[i, -1])
        if len(index[0]) > 0:
            return (index[0][0], i)
    return


def nearest(edge, weight, x, i, k):

    queue = [[i]]
    visited = set([i])
    findPath = []
    while len(queue) > 0:
        path = queue.pop()
        node = path[-1]
        visited.add(node)
        if node == k:
            findPath = path
            break
        for next_node in edge[node]:
            if next_node not in visited:
                queue.append(path + [next_node])

    dist = 0
    for k in range(len(findPath) - 1):
        i, j = findPath[k], findPath[k + 1]
        if dist + weight[(i, j)] > x:
            return (i, j, x - dist, dist + weight[(i, j)] - x)
        dist += weight[(i, j)]


def AdditivePhylogeny(matrix, n, n1):

    if n == 2:
        edge = {}
        edge[0] = [1]
        edge[1] = [0]
        weight = {}
        weight[(0, 1)] = matrix[0, 1]
        weight[(1, 0)] = matrix[0, 1]
        # print(weight)
        return (edge, weight, n1)

    limb = LimbLength(matrix, n - 1)
    # print(limb)
    matrix[:n-1, n-1] -= limb
    matrix[n-1, :n-1] -= limb
    i, k = FindingIAndK(matrix)
    x = matrix[i, n-1]
    # print(i)
    # print(k)
    # print(matrix)
    # print(matrix[i,-1])
    # print(x)
    edge, weight, n1 = AdditivePhylogeny(matrix[:n-1, :n-1], n - 1, n1)
    i_Prime, k_Prime, i_x, n_x = nearest(edge, weight, x, i, k)
    new_node = i_Prime

    if i_x != 0:
        new_node = n1
        n1 += 1
        edge[i_Prime].remove(k_Prime)
        edge[k_Prime].remove(i_Prime)
        edge[i_Prime].append(new_node)
        edge[k_Prime].append(new_node)
        edge[new_node] = [i_Prime, k_Prime]

        weight[(new_node, i_Prime)] = i_x
        weight[(i_Prime, new_node)] = i_x
        weight[(new_node, k_Prime)] = n_x
        weight[(k_Prime, new_node)] = n_x
        del weight[(i_Prime, k_Prime)]
        del weight[(k_Prime, i_Prime)]
    edge[new_node].append(n - 1)
    edge[n - 1] = [new_node]
    weight[(n - 1, new_node)] = limb
    weight[(new_node, n - 1)] = limb
    return (edge, weight, n1)


f = open("/Users/sara/Desktop/temp.txt")
for i, line in enumerate(f):
        line = line.strip()
        if i == 0:
            n = int(line)
            # print(dim)
            matrix = np.zeros((n, n), dtype=np.int32)
            # print(matrix)
        else:
            # print(i)
            rowData = np.array(line.split()).astype(np.int32)
            # print(rowData)
            matrix[i - 1] += rowData
            # print(matrix)

edge, weight, t = AdditivePhylogeny(matrix, n, n)
for i in sorted(edge):
    for j in (edge[i]):
        print(str(i) + "->" + str(j) + ":" + str(weight[(i, j)]))