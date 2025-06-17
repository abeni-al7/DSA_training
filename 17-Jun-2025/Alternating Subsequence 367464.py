# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    if n == 0:
        print(0)
        continue
    total = 0
    cur_max = a[0]
    for i in range(1, n):
        if (a[i] > 0) == (a[i-1] > 0):
            if a[i] > cur_max:
                cur_max = a[i]
        else:
            total += cur_max
            cur_max = a[i] 
    total += cur_max
    print(total)