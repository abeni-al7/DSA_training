class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        z = 0
        x = 0
        for num in nums:
            x ^= num
            if num == 0:
                z += 1
        if x != 0:
            return n
        if z == n:
            return 0
        else:
            return n - 1