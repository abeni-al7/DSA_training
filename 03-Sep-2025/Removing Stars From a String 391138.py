# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        k = 0
        for char in s:
            if char == "*":
                k -= 1
            else:
                s[k] = char
                k += 1
        return "".join(s[:k])