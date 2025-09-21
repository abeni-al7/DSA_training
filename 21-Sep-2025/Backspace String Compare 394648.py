# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for char in s:
            if s_stack and char == "#":
                s_stack.pop()
            elif char != "#":
                s_stack.append(char)
        
        for char in t:
            if t_stack and char == "#":
                t_stack.pop()
            elif char != "#":
                t_stack.append(char)
        
        return s_stack == t_stack
        