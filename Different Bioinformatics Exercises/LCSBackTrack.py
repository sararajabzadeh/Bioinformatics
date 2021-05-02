def LCSBackTrack(v, w):
    matrix = [[0 for x in range(len(w)+1)] for y in range(len(v)+1)]
    Backtrack = [[0 for x in range(len(w)+1)] for y in range(len(v)+1)]
    # for i in range(len(v)):
    #     matrix[i][0]= 0
    # for j in range(len(w)):
    #     matrix[0][j] = 0
    for i in range(1 , len(v)+1):
        for j in range(1,len(w)+1):
            match = 0
            if v[i - 1] == w[j-1]:
                match = 1
            matrix[i][j] = max(matrix[i - 1][j],matrix[i][j - 1],matrix[i - 1][j - 1] + match)
            if matrix[i][j] == matrix[i-1][j]:
                Backtrack[i][j] = "↓"
            elif matrix[i][j] == matrix[i][j-1]:
                Backtrack[i][j] = "→"
            elif matrix[i][j] == matrix[i-1][j-1] + match:
                Backtrack[i][j] = "↘"
            print(matrix)
    return Backtrack

v = input()
w = input()
print(LCSBackTrack(v , w))