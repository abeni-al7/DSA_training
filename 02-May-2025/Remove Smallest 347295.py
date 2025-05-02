# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    pos = True
    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            print("NO")
            pos = False
            break
    if pos:
        print("YES")