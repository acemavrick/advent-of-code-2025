with open("6.txt") as f:
    math = f.readlines()
column_list = {}
for l in math:
    c = 0
    for v in l.strip().split(" "):
        if v != "" and not column_list.get(c):
            column_list[c] = [v]
            c += 1
        elif v != "":
            column_list[c].append(v)
            c += 1
t = 0
for i in column_list.values():
    nums = [int(v) for v in i[:-1]]
    value = 0
    if i[-1] == "*":
        value = 1
        for v in nums:
            value *= v
    elif i[-1] == "+":
        value = sum(nums)
    t += value
print(t)