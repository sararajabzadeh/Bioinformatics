def BWT(string):
    array = [string]
    for i in range(len(string)-1):
        string = string[len(string)-1] + string[:len(string)-1]
        array+=[string]
    array.sort()
    array2 = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            array2+= array[i][len(array[0])-1]
            break
    return array2
string = input()

print(BWT(string))
