import math

with open("input/d6.in") as f:
    lines = [line.rstrip() for line in f.readlines()]

ops = lines[-1]
nums = lines[:-1]
# find indices of non-space characters in ops
op_indices = [i for i, c in enumerate(ops) if c != " "]
# split each line in nums at op_indices
data = []
for line in nums:
    splitted = list(line)
    for i in op_indices:
        if i == 0:
            continue
        splitted[i-1] = "*"
    data.append("".join(splitted).split("*"))
# print(data)
cols = []
ops = [c for c in ops if c != " "]
# print(ops)
for i in range(len(ops)):
    ccol = [l[i] for l in data]
    pad = max(len(x) for x in ccol)
    # we pad on the right bc we used rstrip
    ccol = [x.ljust(pad, " ") for x in ccol]
    ncol = []
    for i in range(pad):
        num_str = "".join(row[i] for row in ccol).rstrip()
        ncol.append(int(num_str) if num_str else 0)
    cols.append(ncol)

        
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