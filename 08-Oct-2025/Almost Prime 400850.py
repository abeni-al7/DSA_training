# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def count_factors(n):
  d = 2
  num = n
  factors = set()

  while d * d <= n:
    while num % d == 0:
      num //= d
      factors.add(d)
    d += 1
  if num > 1:
    factors.add(num)
  return len(factors) == 2

n = int(input())
count = 0
for i in range(1, n+1):
  if count_factors(i):
    count += 1
print(count)