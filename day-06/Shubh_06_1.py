import re
import math

with open("input/d6s.in") as f:
    lines = f.readlines()

data = [re.sub(" +", " ", line).strip().split(" ") for line in lines]
probs = [[int(x) for x in line] for line in data[:-1]]
ops = data[-1]

cols = [list(col) for col in zip(*probs)]

for col in range(len(cols)):
    if ops[col] == "*":
        # multiply all elements in the column
        cols[col] = math.prod(cols[col])
    elif ops[col] == "+":
        # sum all elements in the column
        cols[col] = sum(int(x) for x in cols[col])
    else:
        raise ValueError("Invalid operation")

print(sum(cols))