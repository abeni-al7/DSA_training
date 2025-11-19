# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

from collections import defaultdict
t = int(input())


def find(x, parent):
    path = []
    while x != parent[x]:
        path.append(x)
        x = parent[x]
    for item in path:
        parent[item] = x
    return x


def union(x, y, parent, n):
    if x < 0 or y < 0 or x >= n or y >= n:
        return
    parX, parY = find(x, parent), find(y, parent)
    if parX != parY:
        parent[parY] = parX


for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    t = input()

    parent = {i: i for i in range(n)}
    for i in range(n):
        union(i, i + k, parent, n)
        union(i, i + k + 1, parent, n)
        union(i, i - k, parent, n)
        union(i, i - k - 1, parent, n)

    components = defaultdict(list)
    for i in range(n):
        root = find(i, parent)
        components[root].append(i)

    for k, v in components.items():
        s_candidates = []
        t_candidates = []
        for i in range(len(v)):
            s_candidates.append(s[v[i]])
            t_candidates.append(t[v[i]])
        if sorted(s_candidates) != sorted(t_candidates):
            print("NO")
            break
    else:
        print("YES")
