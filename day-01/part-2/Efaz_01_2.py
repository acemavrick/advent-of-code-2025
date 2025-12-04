import os
import math

current = 50
cwd = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cwd, "1.txt")) as f:
    lines = f.readlines()
count = 0
for i in lines:
    mag = int(i[1:])
    direction = i[0]
    for i in range(mag):
        if direction.startswith("L"):
            current = math.floor(current - 1) % 100
        else:
            current = math.floor(current + 1) % 100
        if current == 0:
            count += 1
    current %= 100
print(count)