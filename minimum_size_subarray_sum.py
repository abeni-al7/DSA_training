class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, total = 0, 0
        minLength = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minLength = min(r - l + 1, minLength)
                total -= nums[l]
                l += 1
        return 0 if minLength == float('inf') else minLength
