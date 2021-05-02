def Complement(Pattern):
    word =""
    for char in Pattern:
        if char=="A":
            word = word+"T"
        elif char=="T":
            word = word +"A"
        elif char=="C":
            word = word +"G"
        elif char=="G":
            word = word +"C"
    return word
Pattern = input()
print(Complement(Pattern))




