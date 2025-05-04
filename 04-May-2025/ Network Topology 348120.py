# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict
n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

one_edge = 0
two_edges = 0
star = 0
unknown = False

for i in range(1, n+1):
    if len(graph[i]) == 1:
        one_edge += 1
    elif len(graph[i]) == 2:
        two_edges += 1
    elif len(graph[i]) == n - 1:
        star += 1
    else:
        unknown = True

if unknown:
    print("unknown topology")
elif star == 1 and one_edge == n - 1:
    print("star topology")
elif one_edge == 0 and two_edges == n:
    print("ring topology")
elif two_edges == n - 2 and one_edge == 2:
    print("bus topology")
else:
    print("unknown topology")
    