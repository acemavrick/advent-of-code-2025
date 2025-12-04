with open("3.txt") as f:
    banks = f.readlines()
jolts = 0
for i in banks:
    i = list(i.strip())
    trim = len(i) - 12
    coll = []
    for ch in i:
        while coll and trim > 0 and coll[-1] < ch:
            coll.pop()
            trim -= 1
        coll.append(ch)
    if trim > 0:
        coll = coll[:-trim]
    jolts += int("".join(coll[:12]))
print(jolts)