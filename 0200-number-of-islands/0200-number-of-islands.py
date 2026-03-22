class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        inbound = lambda x, y: 0 <= x < rows and 0 <= y < cols
        count = 0
        visited = set()

        def bfs(i, j):
            queue = deque([(i, j)])

            while queue:
                i, j = queue.popleft()
                visited.add((i, j))
                
                for x, y in directions:
                    new_i, new_j = i + x, j + y
                    if inbound(new_i, new_j) and grid[new_i][new_j] == "1":
                        if (new_i, new_j) not in visited:
                            queue.append((new_i, new_j))
                            visited.add((new_i, new_j))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    count += 1
        
        return count
        
