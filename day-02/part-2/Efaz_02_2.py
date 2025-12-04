with open("2.txt") as f:
    line = f.readline()
ids = line.strip().split(",")
sum = 0
for i in ids:
    sect1, sect2 = i.split("-")
    sect1, sect2 = int(sect1), int(sect2)
    for j in range(sect1, sect2+1):
        c = False
        s = str(j)
        for k in range(1, (len(s)//2)+1):
            if len(s) % k != 0:
                continue
            code = s[:k]
            if code * (len(s)//k) == s:
                c = True
                break
        if c:
            sum += j
print(sum)