with open("6.txt") as f:
    math = f.readlines()
column_list = {}
for l in math:
    c = 0
    for v in l:
        if not column_list.get(c):
            column_list[c] = []
        column_list[c].append(v)
        c += 1
reformatted_list = {}
ind = 0
c = 0
op = ""
for i, v in column_list.items():
    nums = v[:-1]
    x = [" ", "\n"]
    if not reformatted_list.get(ind):
        reformatted_list[ind] = []
    if [" "] * len(nums) == nums or ["\n"] * len(nums) == nums:
        reformatted_list[ind].append(op)
        ind += 1
        op = ""
        continue
    nums = int("".join(nums))
    if v[-1] != " ":
        op = v[-1]
    reformatted_list[ind].append(str(nums))
    c += 1
t = 0
for i in reformatted_list.values():
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