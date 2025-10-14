# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}
        max_len = 0
        for num in arr:
            if num - difference in memo:
                memo[num] = 1 + memo[num - difference]
            else:
                memo[num] = 1
            max_len = max(max_len, memo[num])
        return max_len