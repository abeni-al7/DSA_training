# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] != a[2]:
        print("NO")
    else:
        print("YES")