# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pos_count = [0] * 32
    for i in range(32):
        for num in a:
            if num & (1 << i):
                pos_count[i] += 1
    
    ans = [1]
    for i in range(1, n):
        ind = i + 1
        for val in pos_count:
            if val % ind != 0:
                break
        else:
            ans.append(ind)
    print(*ans)