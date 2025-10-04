# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)
        memo = {}

        def dp(i, jump):
            if i == stones[-1]:
                return True
            elif i not in stones_set or jump == 0:
                return False
            
            if (i, jump) in memo:
                return memo[(i, jump)]
            
            memo[(i, jump)] = dp(i+jump, jump-1) or dp(i+jump, jump) or dp(i+jump, jump+1)
            return memo[(i, jump)]

        return dp(stones[0], 1)