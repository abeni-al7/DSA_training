# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            
            if memo[i] != -1:
                return memo[i]
            
            if i+1 < len(s) and int(s[i:i+2]) < 27:
                memo[i] = dp(i+1) + dp(i+2)
            else:
                memo[i] = dp(i+1)
            return memo[i]
            
        return dp(0)