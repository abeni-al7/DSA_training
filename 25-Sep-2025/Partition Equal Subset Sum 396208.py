# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        memo = {}
        def dp(i, total):
            if i == 0:
                return (total + nums[i] == target) or (total == target)
            if (i, total) not in memo:
                memo[(i, total)] = dp(i - 1, total) or dp(i - 1, total + nums[i])
            return memo[(i, total)]
        return dp(len(nums) - 1, 0)