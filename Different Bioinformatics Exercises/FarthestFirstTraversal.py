import math , copy
k , m = map(int , input().split())
point = input()
array = []
while point != "*":
    array += [point.split(" ")]
    point = input()
# print(array)
for i in range(len(array)):
    for j in range(len(array[0])):
        array[i][j] = float(array[i][j])
# print(array)
distance = []
centers = copy.deepcopy(array[:1])
# print(array)
# print(centers)
clusters = {}

for i in range(len(array)):
    clusters[i]=0
# print(clusters)
index=[0]


while len(centers)<k:
    distance.clear()
    # clusters.clear()
    # for i in range(len(array)):
    #     # distance.clear()
    #     for j in range(len(centers)):
    #         sum = 0
    #         for l in range(m):
    #             sum += (array[i][l] - centers[j][l])**2
    #             # print("sum")
    #             # print(sum)
    #         distance += [math.sqrt(sum)]
    #         # print("distance")
    #         # print(distance)
    # centers += [array[distance.index(max(distance))]]
    # array.pop(distance.index(max(distance)))
    maximum = []
    maxindex = []
    for i in range(len(centers)):
        distance.clear()
        # print("i")
        # print(i)
        for j in range(len(array)):
            sum = 0
            # print("j")
            # print(j)
            if clusters[index[i]]==clusters[j]:
                for l in range(m):
                    # print("l")
                    # print(l)
                    sum += (array[j][l] - centers[i][l]) ** 2
                    # print("sum")
                    # print(sum)
                distance += [math.sqrt(sum)]
                # print("distance")
                # print(distance)
            else:
                distance += [math.sqrt(sum)]
        maximum += [max(distance)]
        maxindex += [distance.index(max(distance))]
        # print("maximums")
        # print(maximum)
        # print(maxindex)
    centers += [array[maxindex[maximum.index(max(maximum))]]]
    index += [maxindex[maximum.index(max(maximum))]]
    # print("centers")
    # print(centers)

    # print(distance)
    # print(array)
    # print(centers)
    for i in range(len(array)):
        distance.clear()
        for j in range(len(centers)):
            sum = 0
            for l in range(m):
                sum += (array[i][l] - centers[j][l]) ** 2
            distance += [math.sqrt(sum)]
        clusters[i] = distance.index(min(distance))
        # print("clusterdistance")
        # print(distance)



    # print("cluster")
    # print(clusters)
for i in range(len(centers)):
    print(*centers[i], sep=" ")