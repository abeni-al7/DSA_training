# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

n, m = map(int, input().split())
first = list(map(int, input().split()))
second = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


result = []
if n == 1:
    for num in second:
        result.append(first[0] + num)
else:
    g = 0
    for i in range(1, n):
        val = first[i] - first[0]
        g = gcd(g, val)

    for num in second:
        result.append(abs(gcd(first[0] + num, g)))

print(*result)
