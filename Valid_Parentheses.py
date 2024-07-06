class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                a = stack.pop()
                if char != brackets[a]:
                    return False
        return stack == []
        
