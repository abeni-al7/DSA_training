# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

n, m, k = map(int, input().split())
if k > 0:
    governments = set(map(int, input().split()))
else:
    governments = set()

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n + 1)

gov_comp_sizes = []

free_nodes_count = 0


def get_component_info(node):
    stack = [node]
    visited[node] = True
    size = 0
    has_gov = False

    while stack:
        curr = stack.pop()
        size += 1
        if curr in governments:
            has_gov = True

        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
    return size, has_gov


for i in range(1, n + 1):
    if not visited[i]:
        size, has_gov = get_component_info(i)
        if has_gov:
            gov_comp_sizes.append(size)
        else:
            free_nodes_count += size

gov_comp_sizes.sort(reverse=True)

if gov_comp_sizes:
    gov_comp_sizes[0] += free_nodes_count
else:
    gov_comp_sizes.append(free_nodes_count)

max_edges = 0
for size in gov_comp_sizes:
    max_edges += (size * (size - 1)) // 2

print(max_edges - m)
