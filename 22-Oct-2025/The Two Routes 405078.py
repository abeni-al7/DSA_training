# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

from collections import deque


def bfs(graph, n):
    dist = [-1] * (n + 1)
    dist[1] = 0
    queue = deque([1])

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if dist[child] == -1:
                dist[child] = dist[node] + 1
                queue.append(child)
    return dist[n]


n, m = map(int, input().split())
rail_graph = [[] for _ in range(n + 1)]
road_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    rail_graph[u].append(v)
    rail_graph[v].append(u)

rail_set = [set(val) for val in rail_graph]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j not in rail_set[i]:
            road_graph[i].append(j)
            road_graph[j].append(i)

rail = bfs(rail_graph, n)
road = bfs(road_graph, n)

if road == -1 or rail == -1:
    print(-1)
else:
    print(max(road, rail))