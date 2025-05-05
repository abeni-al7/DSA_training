# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[-1])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inbound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        fresh = 0
        queue = deque()
        time = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append([row, col])
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for direction in directions:
                    new_r, new_c = r + direction[0], c + direction[1]
                    if inbound(new_r, new_c) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append([new_r, new_c])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
        