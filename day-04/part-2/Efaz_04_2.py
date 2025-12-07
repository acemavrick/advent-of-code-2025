with open("4.txt") as f:
    aisles = f.readlines()
total_rolls = 0
while True:
    rolls = 0
    row_num = 0
    for i in aisles:
        i = i.strip()
        l = list(i)
        for j in range(len(i)):
            if not i[j] == "@":
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
                l[j] = "."
                i = "".join(l)
                aisles[row_num] = "".join(l)
                rolls += 1
        row_num += 1
    if rolls == 0:
        break
    total_rolls += rolls
print(total_rolls)