# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        a = list(map(int, input().split()))
        matrix.append(a)
    
    inbound = lambda r, c: 0 <= r < n and 0 <= c < m
    directions = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    max_sum = 0
    for i in range(n):
        for j in range(m):
            current_sum = matrix[i][j]
            for dr, dc in directions:
                r, c = i + dr, j + dc
                while inbound(r, c):
                    current_sum += matrix[r][c]
                    r += dr
                    c += dc
            max_sum = max(max_sum, current_sum)
    print(max_sum)