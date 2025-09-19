# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = []
 
        for d in dirs:
            if d == ".." and stack:
                stack.pop()
            elif d in [".", "", ".."]:
                continue
            else:
                stack.append(d)
        return "/" + "/".join(stack)