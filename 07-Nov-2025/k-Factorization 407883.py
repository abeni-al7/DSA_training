# Problem: k-Factorization - https://codeforces.com/problemset/problem/797/A

n, k = map(int, input().split())
i = 2

vals = []
while n > 1 and k > 1:
    while n % i:
        i += 1
    n //= i
    vals.append(i)
    k -= 1
if n > 1:
    vals.append(n)
    k -= 1

if k > 0:
    print(-1)
else:
    print(*vals)
