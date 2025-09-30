# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1


        ans = [[0] * n for _ in range(m)]
        ans[0][1] = 1
        ans[1][0] = 1
        
        for i in range(m):
            for j in range(n):
                if (i == 1 and j == 0) or (j == 1 and i == 0):
                    continue
                ans[i][j] = ans[i-1][j] + ans[i][j-1]

        return ans[-1][-1]