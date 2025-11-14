# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parX, parY = self.find(x), self.find(y)
        if parX == parY:
            return False

        self.parent[parX] = parY
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        components = n
        edges = []

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edges.append([cost, i, j])
        edges.sort()

        res = 0
        for i in range(len(edges)):
            c, x, y = edges[i]
            if uf.union(x, y):
                res += c
                components -= 1
                if components == 1:
                    break
        return res