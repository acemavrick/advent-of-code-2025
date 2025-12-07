with open("5.txt") as f:
    ingredients = f.readlines()
range_mode = True
ranges = []
for i in ingredients:
    i = i.strip()
    if i == "":
        range_mode = False
        continue
    if range_mode == True:
        parts = i.split("-")
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))
ranges.sort()
mix = []
for start, end in ranges:
    if not mix or start > mix[-1][1] + 1:
        mix.append([start, end])
    else:
        mix[-1][1] = max(mix[-1][1], end)
print(sum([(end - start + 1) for start, end in mix]))