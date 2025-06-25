# Problem: Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_prefix = 0
        current = 0
        max_sum = float("-inf")
        for num in nums:
            current += num
            max_sum = max(current - min_prefix, max_sum)
            min_prefix = min(min_prefix, current)
        return max_sum