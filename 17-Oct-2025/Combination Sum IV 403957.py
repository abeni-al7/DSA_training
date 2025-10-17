# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(curr):
            if curr == 0:
                return 1
            elif curr < 0:
                return 0
            
            if curr in memo:
                return memo[curr]
            
            result = 0
            for num in nums:
                result += dp(curr - num)
            memo[curr] = result
            return memo[curr]
        return dp(target)
