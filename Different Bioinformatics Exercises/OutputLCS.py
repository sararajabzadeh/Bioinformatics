import sys

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
    # print(matrix)
    return Backtrack

def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == "↓":
        return OutputLCS(backtrack, v, i - 1, j)
    elif backtrack[i][j] == "→":
        return OutputLCS(backtrack, v, i, j - 1)
    else:
        return OutputLCS(backtrack, v, i - 1, j - 1) + v[i-1]

v = input()
w = input()
# print(LCSBackTrack(v , w))
sys.setrecursionlimit(1500)
if len(v)>=len(w):
    backtrack = LCSBackTrack(v , w)
    print(OutputLCS(backtrack, v, len(v), len(w)))

else:
    backtrack = LCSBackTrack(w , v)
    print(OutputLCS(backtrack, w, len(w), len(v)))
