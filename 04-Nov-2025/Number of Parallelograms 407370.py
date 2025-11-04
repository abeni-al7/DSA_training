# Problem: Number of Parallelograms - https://codeforces.com/contest/660/problem/D

from collections import defaultdict

n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

M = 2 * 10**9 + 1
midpoints = defaultdict(int)
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if i == j:
            continue
        midpoints[
            (points[i][0] + points[j][0]) * M + (points[i][1] + points[j][1])
        ] += 1

count = 0
for k, v in midpoints.items():
    count += v * (v - 1) // 2
print(count)