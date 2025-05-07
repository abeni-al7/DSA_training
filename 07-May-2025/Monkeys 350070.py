# Problem: Monkeys - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/E

n, m = map(int, input().split())
edges = []

for _ in range(n):
    left, right = map(int, input().split())
    edges.append((left, right))

removed = []
for _ in range(m):
    monkey, hand = map(int, input().split())
    removed.append((monkey, hand))
removed_set = set(removed)

# init union find
parent = {node: node for node in range(1, n + 1)}
time = {node: float('inf') for node in range(1, n + 1)}

def get(node):
    if node == parent[node]:
        return node, time[node]
    parent[node], parent_time = get(parent[node])
    time[node] = min(time[node], parent_time)
    return parent[node], time[node]

def union(node1, node2, t):
    parent1, time1 = get(node1)
    parent2, time2 = get(node2)
    if parent1 != parent2:
        if parent1 == 1:
            parent[parent2] = parent1
            time[parent2] = min(t, time[parent2])
        else:
            parent[parent1] = parent2
            time[parent1] = min(t, time[parent1])

for i, (left, right) in enumerate(edges):
    if left != -1 and (i + 1, 1) not in removed_set:
        union(i + 1, left, float('inf'))
    if right != -1 and (i + 1, 2) not in removed_set:
        union(i + 1, right, float('inf'))

for i, (monkey, hand) in enumerate(removed[::-1]):
    t = m - i - 1
    union(monkey, edges[monkey - 1][hand - 1], t)

for node in range(1, n + 1):
    t = get(node)[1]
    if t == float('inf'):
        print(-1)
    else:
        print(t)