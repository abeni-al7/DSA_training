# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

n, m = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
        self.score = [0] * (n + 1)
        self.diff = [0] * (n + 1)

    def find(self, x):
        if x != self.parent[x]:
            orig_parent = self.parent[x]
            self.parent[x] = self.find(self.parent[x])
            self.diff[x] += self.diff[orig_parent]
        return self.parent[x]

    def union(self, x, y):
        parX, parY = self.find(x), self.find(y)
        if parX == parY:
            return
        if self.size[parX] >= self.size[parY]:
            self.parent[parY] = parX
            self.size[parX] += self.size[parY]
            self.diff[parY] = self.score[parY] - self.score[parX]
        else:
            self.parent[parX] = parY
            self.size[parY] += self.size[parX]
            self.diff[parX] = self.score[parX] - self.score[parY]

    def add(self, x, val):
        parX = self.find(x)
        self.score[parX] += val


uf = UnionFind(n)
for _ in range(m):
    curr = input().split()
    if curr[0] == "join":
        uf.union(int(curr[1]), int(curr[2]))
    elif curr[0] == "add":
        uf.add(int(curr[1]), int(curr[2]))
    else:
        uf.find(int(curr[1]))
        print(uf.score[uf.parent[int(curr[1])]] + uf.diff[int(curr[1])])
