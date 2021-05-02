def MiddleEdge(v , w):
    middle = int(len2/2)
    v1 = v[:middle]
    v2 = v[middle+1::-1]
    w1 = w[::1]
    w2 = w[::-1]

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


    source = Score(v1 , w1)
    TempSink = Score(v2 , w2)
    sink=[]
    for i in range(len(TempSink)-1,-1,-1):
        sink += [TempSink[i]]

    scr1 = [source[i] + sink[i] - 5 for i in range(len(w))]
    diagnal = [score[dic[v[middle]]][dic[w[i-1]]] for i in range(1, len(w))]
    scr2 = [source[i-1] + sink[i] + diagnal[i-1] for i in range(1, len(w))]
    maximum = max(max(scr1) , max(scr2))
    if maximum==max(scr1):
        index1 = scr1.index(maximum)
        index2 = scr1.index(maximum)
    else:
        index1 = scr2.index(maximum)-1
        index2 = scr2.index(maximum)
    return (index1 , middle , index2,middle+1)


def Score(v , w):
    # matrix = [[0 for x in range(len1 + 1)] for y in range(len1 + 1)]
    # for i in range(1,len(v)+1):
    #     matrix[i][0] -= 5
    # for j in range(1,len(w)+1):
    #     matrix[0][j] -= 5

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

    Pscore = [0]*(len1+1)
    Cscore = [0]*(len1+1)
    for i in range(1,len(w)+1):
        Pscore[i] = Pscore[i-1]-5
    for i in range(1,len(v)+1):
        Cscore[0] = i*(-5)
        for j in range(1,len(w)+1):
            top = Cscore[j-1]-5
            left = Pscore[j]-5
            diag = Pscore[j-1]+score[dic[v[i-1]]][dic[w[j-1]]]
            Cscore[j] = max(top,left,diag)
        Pscore = Cscore
    return Pscore
    # for i in range(1,len(v)+1):
    #     for j in range(1,len(w)+1):
    #         matrix[i][j]=max(matrix[i-1][j]-5,
    #                          matrix[i][j-1]-5,
    #                          matrix[i-1][j-1]+score[dic[v[i-1]]][dic[w[j-1]]])
    #
    # return matrix[len(v)][:]

def LinearSpaceAlignment(v, w, top, bottom, left, right):
    st1=""
    st2 =""
    if left == right:
        st1 += v[top:bottom]
        for i in range(bottom-top):
            st2+="-"
        # st2 += ("-")*(bottom-top)
        return (-5)*(bottom-top)
    if top == bottom:
        for i in range(left-right):
            st1+="-"
        # st1 += ["-"]*(left-right)
        st2 += w[left-right]
        return (-5)*(left-right)
    middle = (left + right)//2
    midEdge = MiddleEdge(v, w)

    midNode = midEdge[0]
    LinearSpaceAlignment(v, w, top, midNode, left, middle)

    if midEdge[0] == midEdge[2] and midEdge[1] + 1 == midEdge[3]:
        st1 += '-'
        st2 += w[midEdge[1]]
    if midEdge[0] + 1 == midEdge[2] and midEdge[1] == midEdge[3]:
        st1 += v[midEdge[0]]
        st2 += '-'
    else:
        st1 += v[midEdge[0]]
        st2 += w[midEdge[1]]

    LinearSpaceAlignment(v, w, midNode, bottom, middle, right)
    return midEdge


p1 = input()
p2 = input()
len1 = len(p1)
len2 = len(p2)
LinearSpaceAlignment(p2 , p1 , 0 , len2 , 0 , len1)
# print(Score(p2 , p1))