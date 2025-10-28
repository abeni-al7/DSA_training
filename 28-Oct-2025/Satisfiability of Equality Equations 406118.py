# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = {}
        size = {}

        connect = []
        check = []

        for e in equations:
            a, op, b = e[:1], e[1:3], e[3:]
            root[a], root[b] = a, b
            size[a] = size[b] = 1
            if op == "==":
                connect.append((a, b))
            else:
                check.append((a, b))

        for a, b in connect:
            self.union(a, b, root, size)
        
        for a, b in check:
            if self.get(a, root) == self.get(b, root):
                return False
        return True
        
    def get(self, node, root):
        if node != root[node]:
            root[node] = self.get(root[node], root)
        return root[node]
    
    def union(self, x, y, root, size):
        parX = self.get(x, root)
        parY = self.get(y, root)

        if parX == parY:
            return
        if size[parX] >= size[parY]:
            root[parY] = parX
            size[parX] += size[parY]
        else:
            root[parX] = parY
            size[parY] += size[parX]