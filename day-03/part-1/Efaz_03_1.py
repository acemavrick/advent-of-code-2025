with open("3.txt") as f:
    banks = f.readlines()
jolts = 0
for i in banks:
    i = i.strip()
    ind = 0
    largest = 0
    for j in i:
        num = int(j)
        for k in range(ind+1, len(i)):
            num2 = int(i[k])
            combined = int(j + i[k])
            if largest < combined:
                largest = combined
        ind += 1
    jolts += largest
print(jolts)