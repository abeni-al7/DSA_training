class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        uniques = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            if s[r] not in uniques:
                uniques.add(s[r])
                longest = max(longest, r - l + 1)
            else:
                while s[l] != s[r]:
                    uniques.remove(s[l])
                    l += 1
                l += 1
        return longest
        
