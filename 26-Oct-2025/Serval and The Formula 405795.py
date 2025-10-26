# Problem: Serval and The Formula - https://codeforces.com/problemset/problem/2085/C

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    if x == y:
        print(-1)
    else:
        print((1 << 49) - max(x, y))