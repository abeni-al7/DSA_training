# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, current):
            if i == 0 and (current + nums[i] == target and current - nums[i] == target):
                return 2
            elif i == 0 and (current + nums[i] == target or current - nums[i] == target):
                return 1
            elif i == 0:
                return 0
            
            if (i, current) not in memo:
                memo[(i, current)] = dp(i-1, current + nums[i]) + dp(i-1, current - nums[i])
            return memo[(i, current)]
        return dp(len(nums)-1, 0)