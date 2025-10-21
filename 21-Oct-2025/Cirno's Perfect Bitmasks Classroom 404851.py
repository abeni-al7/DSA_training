# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())

for _ in range(t):
    x = int(input())
    y = 0

    and_valid = False
    xor_valid = False
    xor_modified = -1
    for i in range(32):
        if (x >> i) & 1 and not and_valid:
            y |= 1 << i
            and_valid = True
            and_modified = i
        elif (x >> i) & 1:
            if xor_valid:
                y &= ~(1 << xor_modified)
            xor_valid = True
            xor_modified = i
        elif not (x >> i) & 1 and not xor_valid:
            y |= 1 << i
            xor_valid = True
            xor_modified = i
    print(y)
