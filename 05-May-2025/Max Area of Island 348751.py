# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        rows, cols = len(grid), len(grid[-1])
        max_area = 0
        inbound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    area = 0
                    queue.append([row, col])
                    visited.add((row, col))
                    while queue:
                        r, c = queue.popleft()
                        area += 1
                        for direction in directions:
                            new_r, new_c = r + direction[0], c + direction[1]
                            if (new_r, new_c) not in visited and inbound(new_r, new_c) and grid[new_r][new_c] == 1:
                                visited.add((new_r, new_c))
                                queue.append([new_r, new_c])
                    max_area = max(area, max_area)
        return max_area