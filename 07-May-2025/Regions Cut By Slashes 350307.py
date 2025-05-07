# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class UnionFind:
    def __init__(self, rows, cols):
        self.parent = {(row, col): (row, col) for row in range(rows) for col in range(cols)}
        self.size = {(row, col): 1 for row in range(rows) for col in range(cols)}
    
    def get(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.get(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        par1 = self.get(node1)
        par2 = self.get(node2)
        if par1 != par2:
            if self.size[par1] >= self.size[par2]:
                self.parent[par2] = par1
                self.size[par1] += self.size[par2]
            else:
                self.parent[par1] = par2
                self.size[par2] += self.size[par1]


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        num_grid = [[0 for _ in range(len(grid) * 3)] for _ in range(len(grid) * 3)]
        for row in range(len(grid)):
            for col in range(len(grid)):
                new_r, new_c = row * 3, col * 3
                if grid[row][col] == "/":
                    num_grid[new_r][new_c+2] = 1
                    num_grid[new_r+1][new_c+1] = 1
                    num_grid[new_r+2][new_c] = 1
                elif grid[row][col] == "\\":
                    num_grid[new_r][new_c] = 1
                    num_grid[new_r+1][new_c+1] = 1
                    num_grid[new_r+2][new_c+2] = 1

        rows, cols = len(num_grid), len(num_grid[-1])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        inbound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        uf = UnionFind(rows, cols)
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if num_grid[r][c] == 0:
                    visited.add((r, c))
                    for direction in directions:
                        new_r, new_c = r + direction[0], c + direction[1]
                        if inbound(new_r, new_c) and num_grid[new_r][new_c] == 0:
                            if (new_r, new_c) not in visited:
                                uf.union((r, c), (new_r, new_c))
        print(uf.parent)
        regions = 0
        for r in range(rows):
            for c in range(cols):
                if num_grid[r][c] == 0 and uf.get((r, c)) == (r, c):
                    regions += 1
        
        return regions