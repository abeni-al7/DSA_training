class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = defaultdict(int) # contains the count of characters in a window
        max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # Shrink the window from the left until a non-repeating character window is achieved
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        return max_length

"""
s = "abcabcbb"
            l
             r

max = 3
counter = {a: 0, b: 1, c: 0}
"""