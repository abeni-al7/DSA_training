# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        def dp(i, j):
            if i != len(s) and j == len(s):
                return False
            if i == len(s) and j == len(s):
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i:j+1] not in words:
                memo[(i, j)] = dp(i, j+1)
            else:
                memo[(i, j)] = True and (dp(j+1, j+1) or dp(i, j+1))

            return memo[(i, j)]
            
        return dp(0, 0)