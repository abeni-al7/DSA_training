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
        if self.size[parX] >= self.size[parY]:
            self.parent[parY] = parX
            self.size[parX] += self.size[parY]
        else:
            self.parent[parX] = parY
            self.size[parY] += self.size[parX]
    
    def components(self):
        components = defaultdict(list)
        for i, v in enumerate(self.parent):
            components[v].append(i)
        return components

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            uf.union(a, b)
        
        count = 0
        components = uf.components()
        for comp, items in components.items():
            size = len(items)
            complete = True
            for node in items:
                if len(graph[node]) != size - 1:
                    complete = False
                    break
            if complete:
                count += 1
        return count
