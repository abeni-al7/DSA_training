# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = []
        for dir in dirs:
            if dir == ".." and stack:
                stack.pop()
            elif dir in ["", ".", ".."]:
                continue
            else:
                stack.append(dir)
        return "/" + "/".join(stack)
        