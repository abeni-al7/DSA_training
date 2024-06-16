class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zeros = 0
        ones = 0
        max_ones = 0
        while l < len(nums) and nums[l] == 0:
            l += 1
        if l >= len(nums):
            return 0
        for r in range(l, len(nums)):
            if nums[r] == 0:
                if zeros > 0:
                    while nums[l] == 1:
                        ones -= 1
                        l += 1
                    l += 1
                else:
                    zeros += 1
            else:
                ones += 1
            max_ones = max(ones, max_ones)
        if l == 0 and zeros == 0:
            max_ones -= 1
        return max_ones
