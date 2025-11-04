# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        def dp(curr, k):
            if k == 0:
                if curr == endPos:
                    return 1
                else:
                    return 0
                
            if (curr, k) in memo:
                return memo[(curr, k)]
            
            left = dp(curr - 1, k - 1) % MOD
            right = dp(curr + 1, k - 1) % MOD
            memo[(curr, k)] = (left + right) % MOD
            return memo[(curr, k)]
            
        return dp(startPos, k)