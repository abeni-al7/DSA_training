# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        current = 0

        i = 0
        while i < len(s):
            if not stack and s[i] == "(":
                current = 1
                stack.append(s[i])
            elif s[i] == "(":
                current *= 2
                stack.append(s[i])
            else:
                score += current
                stack.pop()
                current //= 2
                while i+1 < len(s) and s[i+1] == ")":
                    stack.pop()
                    current //= 2
                    i += 1
            i += 1
        return score