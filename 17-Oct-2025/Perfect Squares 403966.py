# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        memo = [n] * (n + 1)
        memo[0] = 0

        for i in range(1, n + 1):
            for s in range(1, i + 1):
                square = s * s
                if i - square < 0:
                    break
                memo[i] = min(memo[i], 1 + memo[i - square])
        return memo[n]