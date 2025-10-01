# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                prev1 = triangle[i-1][j] if j < len(triangle[i-1]) else float('inf')
                prev2 = triangle[i-1][j-1] if j-1 >= 0 else float('inf')
                triangle[i][j] += min(prev1, prev2)
        return min(triangle[-1])