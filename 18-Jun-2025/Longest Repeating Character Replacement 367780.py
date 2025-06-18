# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        max_len = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while sum(count.values()) - max(count.values()) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len