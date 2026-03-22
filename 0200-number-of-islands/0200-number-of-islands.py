class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        inbound = lambda x, y: 0 <= x < rows and 0 <= y < cols
        count = 0

        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = "0"

            while queue:
                i, j = queue.popleft()
                
                for x, y in directions:
                    new_i, new_j = i + x, j + y
                    if inbound(new_i, new_j) and grid[new_i][new_j] == "1":
                        queue.append((new_i, new_j))
                        grid[new_i][new_j] = "0"
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        
        return count
        
