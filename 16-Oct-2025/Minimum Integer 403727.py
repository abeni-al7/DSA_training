# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

q = int(input())

for _ in range(q):
    l, r, d = map(int, input().split())
    if d < l or d > r:
        print(d)
    else:
        print(((r // d) * d) + d)
