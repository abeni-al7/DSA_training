# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        
        for i in range(1, len(s)):
            if goal == s[i:] + s[:i]:
                return True
        
        return False