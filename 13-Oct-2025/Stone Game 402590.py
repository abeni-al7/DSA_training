# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        total = sum(piles)
        memo = {}

        def dp(l, r):
            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            even = (r - l) % 2
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            memo[(l, r)] = max(
                left + dp(l + 1, r),
                right + dp(l, r - 1)
            )
            return memo[(l, r)]
        
        return dp(0, n - 1) > total // 2
        
