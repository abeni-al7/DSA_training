class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corresponding = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in corresponding:
                stack.append(char)
            elif stack and char == corresponding[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack