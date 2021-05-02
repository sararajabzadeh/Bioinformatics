string = input()
st = ""
array = []
while st !="*":
    st = input()
    array+=[st]
array.remove(array[len(array)-1])
for i in range(len(string)-len(array[0])+1):
    for j in range(len(array)):
        if string[i:i+len(array[0])]==array[j]:
            print(i)
            break