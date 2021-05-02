string = input()
array = []
for i in range(len(string)):
    if string[i]=="T":
        array+= ["U"]
    else:
        array += [string[i]]
print(*array , sep="")