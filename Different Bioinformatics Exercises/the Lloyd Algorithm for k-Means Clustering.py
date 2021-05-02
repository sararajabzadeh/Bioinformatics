import copy , math
k , m = map(int,input().split())

points=[]
t = input()
sum = 0
distance = []
clusters = {}
# print(clusters)
while t != ".":
    points+=[t]
    t = input()
# print(points)
for i in range(len(points)):
    points[i] = points[i].split(" ")
for i in range(len(points)):
    for j in range(len(points[i])):
        points[i][j] = float(points[i][j])
# print(points)
centers = copy.deepcopy(points[:k])
# print(centers)
for i in range(len(points)):
    distance.clear()
    for j in range(len(centers)):
        sum = 0
        for k in range(m):
            sum += (points[i][k] - centers[j][k])**2
        distance+=[math.sqrt(sum)]
        # print("distance")
        # print(distance)
    # print(distance.index(min(distance)))
    # print(centers[distance.index(min(distance))])
    if distance.index(min(distance)) not in clusters.keys():
        clusters[distance.index(min(distance))] = [points[i]]
    else:
        clusters[distance.index(min(distance))] += [points[i]]
# print(clusters)
centerPrime = copy.deepcopy(centers)
for i in range(len(clusters)):
    # print(i)
    # sum = 0
    for j in range(m):
        sum =0
        for k in range(len(clusters[i])):
            sum += clusters[i][k][j]
        # sum += centers[i][j]
        #     print(sum)
        centers[i][j] = sum/(len(clusters[i]))
# print("centers")
# print(centers)
length = 0
for i in range(len(centers)):
    for j in range(m):
        length += (centers[i][j] - centerPrime[i][j])
# print(length)
# print(points)
while length>0.0000001:
    clusters.clear()
    for i in range(len(points)):
        distance.clear()
        for j in range(len(centers)):
            sum = 0
            for k in range(m):
                # print(points[i][k])
                sum += (points[i][k] - centers[j][k]) ** 2
                # print(sum)
            distance += [math.sqrt(sum)]
            # print(i)
            # print("distance")
            # print(distance)
        # print(distance.index(min(distance)))
        # print(centers[distance.index(min(distance))])
        if distance.index(min(distance)) not in clusters.keys():
            clusters[distance.index(min(distance))] = [points[i]]
        else:
            clusters[distance.index(min(distance))] += [points[i]]


        # print(clusters)
    # length = 0.001
    centerPrime = copy.deepcopy(centers)
    for i in range(len(clusters)):
        for j in range(m):
            sum = 0
            for k in range(len(clusters[i])):
                sum += clusters[i][k][j]
            # sum += centers[i][j]
            centers[i][j] = sum / (len(clusters[i]))
    # print("centers")
    # print(centers)
    length = 0
    for i in range(len(centers)):
        for j in range(m):
            length += (abs(centers[i][j] - centerPrime[i][j]))
    # print(length)
# print(centers)
temp = copy. deepcopy(centers)
for i in range(len(centers)):
    for j in range(m):
        temp[i][j] = "{:.3f}".format(round(centers[i][j] , 3))
for i in range(len(temp)):
    print(*temp[i],sep=" ")
#         print(round(centers))
#     print(*round(centers[i] , 3) , sep=" ")
#     temp+=[round(clusters[i] ,3)]