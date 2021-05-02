def LCSBackTrack(v, w , x):
    matrix = [[[0 for i in range(len(x) + 1)] for j in range(len(w) + 1)] for k in range(len(v)+1)]
    Backtrack = [[[0 for i in range(len(x)+1)] for j in range(len(w)+ 1)]for k in range(len(v)+1)]

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            for k in range(1, len(x)+1):
                match = 0
                if v[i-1]==w[j-1]==x[k-1]:
                    match = 1
                matrix[i][j][k] = max(matrix[i-1][j][k],
                                      matrix[i][j-1][k],
                                      matrix[i][j][k-1],
                                      matrix[i-1][j-1][k],
                                      matrix[i-1][j][k-1],
                                      matrix[i][j-1][k-1],
                                      matrix[i - 1][j - 1][k-1]+match)


                if matrix[i][j][k] == matrix[i-1][j-1][k] and i>=1 and j>=1:
                    Backtrack[i][j][k] = "D"
                elif matrix[i][j][k] == matrix[i-1][j][k-1] and i>=1 and k>=1:
                    Backtrack[i][j][k] = "E"
                elif matrix[i][j][k] == matrix[i][j-1][k-1] and j>=1 and k>=1:
                    Backtrack[i][j][k] = "F"
                elif matrix[i][j][k] == matrix[i - 1][j][k] and i>=1:
                    Backtrack[i][j][k] = "A"
                elif matrix[i][j][k] == matrix[i][j - 1][k] and j>=1:
                    Backtrack[i][j][k] = "B"
                elif matrix[i][j][k] == matrix[i][j][k - 1] and k>=1:
                    Backtrack[i][j][k] = "C"
                elif matrix[i][j][k] == matrix[i - 1][j - 1][k-1]+match and i>=1and j>=1 and k>=1:
                    Backtrack[i][j][k] = "G"
    st1 = ""
    st2 = ""
    st3 = ""
    i = len(v)
    j = len(w)
    k = len(x)

    while i>0 :
        # print(st1)
        # print(st2)
        # print(st3)
        if Backtrack[i][j][k]== "G":
            # print("g")
            st1 = v[i-1] + st1
            st2 = w[j-1] + st2
            st3 = x[k-1] + st3
            i -= 1
            j -= 1
            k -= 1
        elif Backtrack[i][j][k]== "A":
            # print("a")
            st1 = v[i-1] + st1
            st2 = "-" + st2
            st3 = "-" + st3
            i -= 1
        elif Backtrack[i][j][k]== "B":
            # print("b")
            st1 = "-" + st1
            st2 = w[j-1] + st2
            st3 = "-" + st3
            j -= 1
        elif Backtrack[i][j][k]== "C":
            # print("c")
            st1 = "-" + st1
            st2 = "-" + st2
            st3 = x[k-1] + st3
            k -= 1
        elif Backtrack[i][j][k]== "D":

            # print("d")
            # print(j)
            st1 = v[i-1] + st1
            st2 = w[j-1] + st2
            st3 = "-" + st3
            i -= 1
            j -= 1
        elif Backtrack[i][j][k]== "E":
            # print("e")
            st1 = v[i-1] + st1
            st2 = "-" + st2
            st3 = x[k-1] + st3
            i -= 1
            k -= 1
        elif Backtrack[i][j][k]== "F":
            # print("f")
            st1 = "-" + st1
            st2 = w[j-1] + st2
            st3 = x[k-1] + st3
            j -= 1
            k -= 1

        else:
            if j>0 and k>0:
                # print("h")
                st1 = v[i-1] + st1
                st2 = w[j-1] +st2
                st3 = x[k-1] +st3
                i -=1
                j -=1
                k-=1
            elif j>0 and k<=1:
                # print("i")
                st1 = v[i-1] +st1
                st2 = w[j-1] +st2
                st3 = "-" + st3
                i-=1
                j-=1
                k-=1
            elif j<=1 and k>0:
                # print("j")
                st1 = v[i-1] +st1
                st2 = "-" + st2
                st3 = x[k-1] +st3
                i-=1
                j-=1
                k-=1
    #
    # print(matrix)
    # print(Backtrack)
    print(matrix[len(v)][len(w)][len(x)])
    print(st1)
    print(st2)
    print(st3)
    return ""


v = input()
w = input()
x = input()


print(LCSBackTrack(v, w , x))


