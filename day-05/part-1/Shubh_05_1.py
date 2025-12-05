with open("input/d5.in") as f:
    content = f.read().strip()

ranges, ids = content.split("\n\n")
ranges = [list(map(int, line.split("-"))) for line in ranges.split("\n")]
ids = [int(line.strip()) for line in ids.split("\n")]

fresh = 0

for i in ids:
    for r in ranges:
        if r[0] <= i <= r[1]:
            fresh += 1
            break

print(fresh) 