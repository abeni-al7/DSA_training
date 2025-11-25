# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class UnionFind:
    def __init__(self, size):
        self.parent = {i: i for i in range(size)}
        self.size = {i: 1 for i in range(size)}
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parX, parY = self.find(x), self.find(y)
        if parX == parY:
            return False
        if self.size[parX] >= self.size[parY]:
            self.parent[parY] = parX
            self.size[parX] += self.size[parY]
        else:
            self.parent[parX] = parY
            self.size[parY] += self.size[parX]
        return True
    

class Solution:
    def diff(self, x, y):
        count = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
        return count

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UnionFind(n)
        groups = n
        for i in range(n):
            for j in range(i + 1, n):
                if strs[i] == strs[j] or self.diff(strs[i], strs[j]) == 2:
                    if uf.union(i, j):
                        groups -= 1
        return groups