# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

import heapq

n, m = map(int, input().split())
edges = []
root = {}
size = {}

for _ in range(m):
    u, v, w = map(int, input().split())
    heapq.heappush(edges, (w, u, v))
    root[u], size[u] = u, 1
    root[v], size[v] = v, 1


def get(node):
    if node != root[node]:
        root[node] = get(root[node])
    return root[node]


def union(u, v):
    parU, parV = get(u), get(v)
    if parU == parV:
        return False
    if size[parU] >= size[parV]:
        root[parV] = parU
        size[parU] += size[parV]
    else:
        root[parU] = parV
        size[parV] += size[parU]
    return True


ans = 0
while edges:
    w, a, b = heapq.heappop(edges)
    if union(a, b):
        ans += w
print(ans)