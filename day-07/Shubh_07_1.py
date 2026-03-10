manifold: list[str] = []
with open("input/d7.in") as file:
    manifold = list(map(str.strip, file.readlines()))
ogO = manifold[0]
manifold = list(map(list, manifold))
manifold[1][ogO.find("S")] = "|"
split = 0
for i in range(2,len(manifold)):
    for j, c in enumerate(manifold[i]):
        if c == "^" and manifold[i-1][j] == "|":
            split += 1
            try:
                manifold[i][j-1] = "|"
            except:
                pass
            try:
                manifold[i][j+1] = "|"
            except:
                pass
        elif c == "." and manifold[i-1][j] == "|":
            manifold[i][j] = "|"
print("\n".join(["".join(l) for l in manifold]))
print(split)