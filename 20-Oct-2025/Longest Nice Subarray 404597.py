# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len = 1
        l = 0

        for r in range(len(nums)):
            for i in range(l, r):
                while nums[r] & nums[i]:
                    l = i + 1
                    break
            else:
                max_len = max(max_len, r - l + 1)

        return max_len
        