with open("5.txt") as f:
    ingredients = f.readlines()
range_mode = True
ranges = []
ingredient_ids = []
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
    else:
        ingredient_ids.append(int(i))
valid = 0
for i in ingredient_ids:
    a = False
    for j in ranges:
        if i >= j[0] and i <= j[1]:
            a = True
            break
    if a:
        valid += 1
print(valid)