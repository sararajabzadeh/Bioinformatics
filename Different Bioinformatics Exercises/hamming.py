in1 = input()
in2 = input()
count = 0
for i in range(len(in1)):
    if in1[i]!= in2[i]:
        count += 1
print(count)