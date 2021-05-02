def SuffixTree(string , SuffixArray , LCP,result  , index):

    for i in range(len(LCP)-1):
        print("i")
        print(i)
        temp = [LCP[i]]
        if LCP[i]==0 and LCP[i+1]!=0:

            j = i+1
            while j!=len(string)-1 and LCP[j]!=0:
                print("j")
                print(j)
                temp+=[LCP[j]]
                j+=1
            print("temp")
            print(temp)
            minimum = min(temp[1:])
            print("minimum")
            print(minimum)
            for k in range(1,len(temp)):
                temp[k] = temp[k] - minimum
            print("temp")
            print(temp)
            print(string[SuffixArray[i]:SuffixArray[i]+minimum])
            return SuffixTree(string,SuffixArray[i:j],temp,result , minimum)
        elif LCP[i]==0 and LCP[i+1]==0:
            print("Hi")
            print(string[SuffixArray[i]:])

    return







string = input()
SuffixArray = input().split(", ")
LCP = input().split(", ")
for i in range(len(SuffixArray)):
    SuffixArray[i] = int(SuffixArray[i])
for i in range(len(LCP)):
    LCP[i] = int(LCP[i])

print(string)
print(SuffixArray)
print(LCP)
print(SuffixTree(string,SuffixArray,LCP , [] , 0))