class UnionFind:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.min_score = [float('inf') for _ in range(n + 1)]
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, x, y, dist):
        parX, parY = self.find(x), self.find(y)
        if self.size[parX] >= self.size[parY]:
            self.parent[parY] = parX
            self.size[parX] += self.size[parY]
            self.min_score[parX] = min(self.min_score[parX], dist)
        else:
            self.parent[parX] = parY
            self.size[parY] += self.size[parX]
            self.min_score[parY] = min(self.min_score[parY], dist)
    
    def findminScore(self):
        init = self.find(1)
        minimum = float('inf')
    
        for i in range(1, len(self.parent)):
            if self.find(i) == init:
                minimum = min(minimum, self.min_score[i])

        return minimum

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a, b, distance in roads:
            uf.union(a, b, distance)
        return uf.findminScore()
        

        