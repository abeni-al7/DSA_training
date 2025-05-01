n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = 0
for r in range(m):
    while l < n and a[l] < b[r]:
        l += 1
    print(l, end=" ")
