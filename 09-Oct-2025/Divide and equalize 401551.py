# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import defaultdict

t = int(input())

def modify_map(n, primes):
    d = 2
    while d * d <= n:
        while n % d == 0:
            primes[d] += 1
            n //= d
        d += 1
    if n > 1:
        primes[n] += 1

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    primes = defaultdict(int)
    for num in nums:
        modify_map(num, primes)
    
    for val in primes.values():
        if val % n != 0:
            print("NO")
            break
    else:
        print("YES")
