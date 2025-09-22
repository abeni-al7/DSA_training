# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        def dp(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0], nums[1])
            
            if n not in self.memo:
                self.memo[n] = max(dp(n-1), nums[n] + dp(n-2))
            return self.memo[n]
        return dp(len(nums) - 1)