# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    a, b = 0, 0
    for char in s:
        if char == ">":
            a += 1
        elif char == "<":
            b += 1
    if a == 0 or b == 0:
        print(n)
    else:
        total, gap = 0, 0
        for char in s:
            if char == "-":
                total += 1
            else:
                if total:
                    gap += total + 1
                total = 0
        if total:
            gap += total + 1
        if s[0] == "-" == s[n-1]:
            gap -= 1
        print(gap)