# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len = 0
        curr = 0
        l = 0
        for r in range(len(nums)):
            while curr & nums[r]:
                curr ^= nums[l]
                l += 1
            max_len = max(max_len, r - l + 1)
            curr |= nums[r]
        return max_len