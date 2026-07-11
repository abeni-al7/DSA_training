class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [1] * n
    
    def find(self, node):
        if self.parent[node] == -1:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node_1, node_2):
        root_1 = self.find(node_1)
        root_2 = self.find(node_2)

        if root_1 == root_2:
            return
        
        if self.size[root_1] > self.size[root_2]:
            self.parent[root_2] = root_1
            self.size[root_1] += self.size[root_2]
        else:
            self.parent[root_1] = root_2
            self.size[root_2] += self.size[root_1]

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        edge_count = {}

        for edge in edges:
            dsu.union(edge[0], edge[1])
        
        for edge in edges:
            root = dsu.find(edge[0])
            edge_count[root] = edge_count.get(root, 0) + 1
        
        complete_count = 0
        for i in range(n):
            if dsu.find(i) == i:
                node_count = dsu.size[i]
                expected_edges = (node_count * (node_count - 1)) // 2
                if edge_count.get(i, 0) == expected_edges:
                    complete_count += 1
        
        return complete_count