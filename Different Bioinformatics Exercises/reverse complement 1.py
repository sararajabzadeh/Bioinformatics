def ReverseComplement(String):
    Result = ""
    for i in range(len(String)-1,-1,-1):
        if String[i]=="A":
            Result+="T"
        elif String[i]=="T":
            Result+="A"
        elif String[i]=="C":
            Result+="G"
        elif String[i]=="G":
            Result+="C"
    return Result

String = input()
print(ReverseComplement(String))