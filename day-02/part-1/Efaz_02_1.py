with open("2.txt") as f:
    line = f.readline()
ids = line.strip().split(",")
sum = 0
for i in ids:
    sect1, sect2 = i.split("-")
    sect1, sect2 = int(sect1), int(sect2)
    for j in range(sect1, sect2+1):
        strin = str(j)
        if strin[:len(strin)//2] == strin[len(strin)//2:]:
            sum += j
print(sum)