with open("input/d12.in", "r") as f:
    lines = list(map(str.strip, f.readlines()))

shapes = []
for _ in range(6):
    z = "".join(lines[:5])
    lines = lines[5:]
    count = z.count("#")
    shapes.append(count)

print(shapes)

tot = 0
for _ in lines:
    dims, cts = map(str.strip, _.split(":"))
    sa, sb = map(int, dims.split("x"))
    area = sa*sb
    totreq = 0
    for a, b in zip(cts.split(" "), shapes):
        totreq += int(a) * b
    if (totreq <= area):
        tot += 1
print(tot)