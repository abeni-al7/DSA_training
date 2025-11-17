# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

n, m = map(int, input().split())
res = []
parent = {i: i for i in range(n + 2)}


def find(x):
    path = []
    while parent[x] != x:
        path.append(x)
        x = parent[x]
    for node in path:
        parent[node] = x
    return x 


for _ in range(m):
    act, node = input().split()
    node = int(node)
    if act == "-":
        parent[node] = find(node + 1)
    else:
        res.append(find(node))

for item in res:
    if item == n + 1:
        item = -1
    print(item)
