
def ManhattanTourist(n, m, Down, Right):
    Matrix = [[0 for x in range(m+1)] for y in range(n+1)]

    for i in range(1,n+1):
        Matrix[i][0] = Matrix[i-1][0] + Down[i-1][0]
    for j in range(1, m+1):
        Matrix[0][j] = Matrix[0][j - 1] + Right[0][j-1]
    for i in range(1, n+1):
        for j in range(1,m+1):
            Matrix[i][j] = max(Matrix[i-1][j]+Down[i-1][j],Matrix[i][j-1]+Right[i][j-1])
    print(Matrix)
    return Matrix[n][m]

n , m = map(int , input().split())
array = [[] for j in range(n)]

array2 = [[] for Y in range(n+1)]
for i in range(n):
    a = list(map(int , input().split()))
    array[i] += a
for i in range(n+1):
    a = list(map(int , input().split()))
    array2[i] += a

print(ManhattanTourist(n , m , array , array2))