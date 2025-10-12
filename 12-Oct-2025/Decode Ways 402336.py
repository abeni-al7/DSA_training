# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [0] * (len(s) + 2)
        memo[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                memo[i] = 0
            elif i+1 < len(s) and int(s[i:i+2]) < 27:
                memo[i] = memo[i+1] + memo[i+2]
            else:
                memo[i] = memo[i+1]
        return memo[0]