def LCSBackTrack(v, w):
    matrix = [[0 for x in range(len(w) + 1)] for y in range(len(v) + 1)]
    Backtrack = [[0 for x in range(len(w) + 1)] for y in range(len(v) + 1)]
    for i in range(1 ,len(v)+1):
        matrix[i][0] = matrix[i-1][0]-5
    for j in range(1, len(w) + 1):
            matrix[0][j] = matrix[0][j-1] - 5

    dic = {"A": 0, "C": 1, "D": 2, "E": 3, "F": 4, "G": 5, "H": 6, "I": 7, "K": 8, "L": 9, "M": 10, "N": 11, "P": 12,
           "Q": 13, "R": 14, "S": 15, "T": 16, "V": 17, "W": 18, "Y": 19}
    score = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
             [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
             [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
             [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
             [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
             [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
             [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
             [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
             [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
             [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
             [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
             [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
             [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
             [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
             [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
             [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
             [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
             [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
             [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
             [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]
             ]


    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            # match = 0
            # if v[i - 1] == w[j - 1]:
            #     match = score[dic[v[i-1]]][dic[w[j-1]]]
            matrix[i][j] = max(matrix[i - 1][j] -5, matrix[i][j - 1] -5 , matrix[i - 1][j - 1] + score[dic[v[i-1]]][dic[w[j-1]]] )
            # print(score[dic[v[i-1]]][dic[w[j-1]]])
            if matrix[i][j] == matrix[i - 1][j]-5:
                Backtrack[i][j] = "↓"
            elif matrix[i][j] == matrix[i][j - 1]-5:
                Backtrack[i][j] = "→"
            elif matrix[i][j] == matrix[i - 1][j - 1] + score[dic[v[i-1]]][dic[w[j-1]]]:
                Backtrack[i][j] = "↘"

    st1 = ""
    st2 = ""
    i = len(v)
    j = len(w)

    while i!=0:

        if Backtrack[i][j]== "↘":
            st1 = v[i-1] + st1
            st2 = w[j-1] + st2
            i -= 1
            j -= 1
        elif Backtrack[i][j]== "→":
            st1 = "-" + st1
            st2 = w[j-1] + st2
            j -= 1
        elif Backtrack[i][j] == "↓":
            st1 = v[i-1] +st1
            st2 = "-" +st2
            i-=1
        else:
            st1 = v[i-1] + st1
            st2 = "-" +st2
            i -=1
            j -=1




    print(Backtrack)
    print(matrix[len(v)][len(w)])
    print(st1)
    print(st2)
    return ""


v = input()
w = input()


resScore = 0
print(LCSBackTrack(v, w))

