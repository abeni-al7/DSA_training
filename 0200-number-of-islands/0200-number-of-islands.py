class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        inbound = lambda x, y: 0 <= x < rows and 0 <= y < cols
        count = 0

        def dfs(i, j):
            if not inbound(i, j):
                return
            if grid[i][j] != "1":
                return
            grid[i][j] = "0"

            for x, y in directions:
                dfs(i + x, j + y)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count
        
