# same as part 1, but we find all possible routes that the beam can take

manifold: list[str] = []
with open("input/d7.in") as file:
    manifold = list(map(str.strip, file.readlines()))
ogO = manifold[0]
manifold = list(map(list, manifold))
manifold[1][ogO.find("S")] = "|"
counts = [[0 for _ in range(len(manifold[-1]))] for _ in range(len(manifold))]
counts[1][ogO.find("S")] = 1  # start with one beam at the source

for i in range(2,len(manifold)):
    for j in range(len(manifold[i])):
        c = manifold[i][j]
        if c == "^" and manifold[i-1][j] == "|":
            counts[i][j-1] += counts[i-1][j]
            counts[i][j+1] += counts[i-1][j]
            manifold[i][j-1] = "|"
            manifold[i][j+1] = "|"
        elif c == "." and manifold[i-1][j] == "|":
            manifold[i][j] = "|"
            counts[i][j] += counts[i-1][j]
        if c == "|" and manifold[i-1][j] == "|":
            manifold[i][j] = "|"
            counts[i][j] += counts[i-1][j]

# final count of beams that reached the bottom
print("\n".join([" ".join(l) for l in manifold]))
print("\n".join([" ".join(map(str, l)) for l in counts]))
print()
beam_total = sum(counts[-1])
print(beam_total)