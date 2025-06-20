# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        count = defaultdict(int)
        letters = len(set(t))
        min_window = float("inf")
        indices = [-1, -1]
        matches = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            if count[s[r]] == target[s[r]]:
                matches += 1
            while matches == letters:
                if r - l + 1 < min_window:
                    min_window = r - l + 1
                    indices = [l, r]
                if count[s[l]] == target[s[l]]:
                    matches -= 1
                count[s[l]] -= 1
                l += 1
        return s[indices[0]:indices[1] + 1] if min_window != float("inf") else ""

