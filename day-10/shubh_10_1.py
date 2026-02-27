# for part 1, only need to press any button 0 or 1 times (bc XOR removes the need to press multiple times)
from copy import deepcopy

with open("input/d10.in") as f:
    lines = [x.strip() for x in f.readlines()]

def apply(state, button):
    for x in button:
        state[x] ^= True
        
tot = 0

for lne in lines:
    lne = lne.split()
    target = tuple(0 if x == '.' else 1 for x in lne[0] if x in '.#')
    stateOG = [0 for _ in target]
    buttons = tuple(tuple(map(int, filter(str.isnumeric, x))) for x in lne[1:-1])

    # brute force
    bstate = 0b0
    minSum = len(buttons)
    while bstate < 1<<len(buttons):
        state = deepcopy(stateOG)
        buttonSet = list(map(int, bin(bstate)[2:].zfill(len(buttons))))
        for i,b in enumerate(buttonSet):
            if b:
                apply(state, buttons[i])
        if (tuple(state) == target):
            print(state, target, sum(buttonSet))
            minSum = min(sum(buttonSet), minSum)
        bstate += 1
    print()
    tot += minSum
print(tot)
    