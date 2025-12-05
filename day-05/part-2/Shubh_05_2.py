with open("input/d5s.in") as f:
    content = f.read().strip()

ranges, ids = content.split("\n\n")
ranges = [list(map(int, line.split("-"))) for line in ranges.split("\n")]
ids = [int(line.strip()) for line in ids.split("\n")]
fresh = set()

merged = []

# merge all intervals
ranges.sort()
for r in ranges:
    if not merged or merged[-1][1] < r[0]:
        merged.append(r)
    else:
        merged[-1][1] = max(merged[-1][1], r[1])

# check ids in merged intervals
tot = 0
for m in merged:
    tot += m[1] - m[0] + 1

print(tot)