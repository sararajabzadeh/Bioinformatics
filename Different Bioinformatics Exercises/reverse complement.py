def reverse(pattern):
    word = ""
    for char in pattern:
        word = char + word
    return word

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

def ReverseComplement(Pattern):
    word = reverse(Pattern)
    result = Complement(word)
    return result

pattern = input()
print(ReverseComplement(pattern))