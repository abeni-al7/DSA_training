# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        memo = {}
        def dp(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return -1
            if i == 0 and j == 0:
                return grid[i][j]
            
            if (i, j) not in memo:
                possible = [x for x in [dp(i-1, j), dp(i, j-1)] if x >= 0]
                memo[(i, j)] = grid[i][j] + min(possible)
            return memo[(i, j)]
        return dp(m-1, n-1)
        