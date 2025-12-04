banks = []
with open("input/d3.in") as file:
    banks = list(map(str.strip, file.readlines()))

out = 0
for b in banks:
    b = list(b)
    count = 0
    lasti = -1
    built = ""
    while count < 12:
        low = lasti+1
        up = len(b) - (11 - count)
        searcheable = b[low:up]
        found = max(searcheable)
        lasti += searcheable.index(found)+1
        built += found
        count += 1
    out += int(built)

print(out)

