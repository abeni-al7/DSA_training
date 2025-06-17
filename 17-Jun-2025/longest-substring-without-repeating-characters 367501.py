# Problem: longest-substring-without-repeating-characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        l = 0
        max_len = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len