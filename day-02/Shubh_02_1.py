with open("input/d2-1.in") as file:
    data = file.readlines()

ranges = [list(map(int, r.split("-"))) for r in data[0].strip().split(",")]

invalids = []

# brute force (with shortcuts)
for r in ranges:
    start_len = len(str(r[0]))
    end_len = len(str(r[1]))

    our_s = r[0]
    our_e = r[1]
    
    if start_len % 2 == 1:
        # bump up to next even length
        our_s = 10**start_len

    if end_len % 2 == 1:
        # bump down to previous even length
        our_e = 10**(end_len - 1) - 1
    
    # split in half to find the lowest half
    half_len = len(str(our_s)) // 2
    lefth = int(str(our_s)[:half_len])
    righth = int(str(our_s)[half_len:])
    lower_code = min(lefth, righth)
    current = lower_code + lower_code * (10**half_len)

    # loop through
    while current <= our_e:
        if current >= our_s:
            # in range
            invalids.append(current)
        # move to next
        lower_code += 1
        current = int(str(lower_code)*2)
    
print(sum(invalids))