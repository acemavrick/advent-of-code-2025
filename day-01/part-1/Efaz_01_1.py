import os
current = 50
cwd = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cwd, "1.txt")) as f:
    lines = f.readlines()
count = 0
for i in lines:
    if i.startswith("L"):
        current -= int(i[1:])
    else:
        current += int(i[1:])
    current %= 100
    if current == 0:
        count += 1
print(count)