# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

n, m, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

ops = []
for _ in range(k):
    op, u, v = input().split()
    ops.append((op, int(u), int(v)))

# DSU setup
parent = [i for i in range(n + 1)]
size = [1] * (n + 1)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]


# Track edges that remain
edge_set = set()
for u, v in edges:
    edge_set.add((min(u, v), max(u, v)))

# Remove cut edges
for op, u, v in ops:
    if op == "cut":
        edge_set.discard((min(u, v), max(u, v)))

# Union remaining edges
for u, v in edge_set:
    union(u, v)

# Process in reverse
ans = []
for op, u, v in reversed(ops):
    if op == "ask":
        ans.append("YES" if find(u) == find(v) else "NO")
    else:
        union(u, v)

print("\n".join(reversed(ans)))
