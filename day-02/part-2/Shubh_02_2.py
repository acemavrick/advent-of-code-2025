with open("input/d2-1.in") as file:
    data = file.readlines()

ranges = [list(map(int, r.split("-"))) for r in data[0].strip().split(",")]

invalids = []

# brute force everything bc why not
for r in ranges:
    # for every number
    for n in range(r[0], r[1] + 1):
        s = str(n)
        l = len(s)

        # loop through every possible repeat length... it will most likely start
        # from the leftmost digit
        is_invalid = False
        for rep_len in range(1, l // 2 + 1):
            if l % rep_len != 0:
                continue
            
            # build the repeated number
            rep_code = s[:rep_len]
            built_num = rep_code * (l // rep_len)
            if built_num == s:
                is_invalid = True
                break

        if is_invalid:
            invalids.append(n)
print(sum(invalids))