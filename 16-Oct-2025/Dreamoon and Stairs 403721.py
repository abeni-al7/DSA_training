# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

n, m = map(int, input().split())

if n < m:
    print(-1)
elif n == m:
    print(n)
else:
    if n % 2 == 0:
        curr = n // 2
    else:
        curr = (n // 2) + 1

    while curr % m != 0:
        curr += 1
    print(curr)   
