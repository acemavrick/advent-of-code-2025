with open("4.txt") as f:
    aisles = f.readlines()
row_num = 0
rolls = 0
for i in aisles:
    i = i.strip()
    for j in range(len(i)):
        l = i[j]
        if not l == "@":
            continue
        adjacent = 0
        if j != len(i)-1 and i[j+1] == "@":
            adjacent += 1
        if j != 0 and i[j-1] == "@":
            adjacent += 1
        if row_num != 0:
            if aisles[row_num-1][j] == "@":
                adjacent += 1
            if j != len(i)-1 and aisles[row_num-1][j+1] == "@":
                adjacent += 1
            if j != 0 and aisles[row_num-1][j-1] == "@":
                adjacent += 1
        if row_num != len(aisles)-1:
            if aisles[row_num+1][j] == "@":
                adjacent += 1
            if j != len(i)-1 and aisles[row_num+1][j+1] == "@":
                adjacent += 1
            if j != 0 and aisles[row_num+1][j-1] == "@":
                adjacent += 1
        if adjacent < 4:
            rolls += 1
    row_num += 1
print(rolls)