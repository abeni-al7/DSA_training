# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        total = sum(piles)
        memo = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i > j:
                    memo[i][j] = 0
                
                even = (j - i) % 2
                left = piles[i] if even else 0
                right = piles[j] if even else 0

                op1 = left + memo[i + 1][j] if i + 1 < n else 0
                op2 = right + memo[i][j - 1] if j - 1 >= 0 else 0
                memo[i][j] = max(op1, op2)
        
        return memo[0][n - 1] > total // 2