class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, x):
        parent = self.parent[x]
        if parent != self.parent[parent]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parX, parY = self.find(x), self.find(y)
        if self.size[parX] <= self.size[parY]:
            self.parent[parY] = parX
            self.size[parX] += self.size[parY]
        else:
            self.parent[parX] = parY
            self.size[parY] += self.size[parX]

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)
        i, j = 0, 1
        while j < len(nums):
            print(i, j)
            l, r = j, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if abs(nums[mid] - nums[i]) <= maxDiff:
                    l = mid + 1
                else:
                    r = mid - 1
            for k in range(i, r + 1):
                uf.union(i, k)
            if r != i:
                i, j = r, r + 1
            else:
                i, j = r + 1, r + 2

        
        answer = []
        for u, v in queries:
            if uf.find(u) == uf.find(v):
                answer.append(True)
            else:
                answer.append(False)
        return answer