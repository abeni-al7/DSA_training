# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

n = int(input())
a = list(map(int, input().split()))

curr = a[0]
while curr % 2 == 0:
    curr //= 2
while curr % 3 == 0:
    curr //= 3

for num in a:
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    if num != curr:
        print("No")
        break
else:
    print("Yes")