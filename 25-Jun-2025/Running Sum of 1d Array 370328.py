# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                running_sum[i] = num
            else:
                running_sum[i] = running_sum[i - 1] + num
        return running_sum