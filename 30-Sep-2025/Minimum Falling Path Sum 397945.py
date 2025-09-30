# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_sum = float('inf')

        memo = {}
        def dp(i, j):
            if i == len(matrix):
                return 0
            
            if j < 0 or j >= len(matrix):
                return float('inf')
            
            if (i, j) not in memo:
                memo[(i, j)] = matrix[i][j] + min(
                    dp(i+1, j-1), dp(i+1, j), dp(i+1, j+1)
                )
            return memo[(i, j)]

        for j in range(len(matrix)):
            min_sum = min(min_sum, dp(0, j))
        return min_sum
