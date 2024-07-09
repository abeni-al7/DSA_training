class Solution:
    def simplifyPath(self, path: str) -> str:
        simple = path.split("/")
        stack = []
        for dir in simple:
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir != "." and dir != "":
                stack.append(dir)
        return "/" + "/".join(stack)
        
