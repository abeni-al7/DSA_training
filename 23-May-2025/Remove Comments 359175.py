# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        code = []
        in_block = False
        cleaned = ""

        for line in source:
            n = len(line)
            i = 0
            while i < n:
                if i + 1 < n and not in_block and line[i] == "/" and line[i + 1] == "*":
                    in_block = True
                    i += 2
                elif i + 1 < n and in_block and line[i] == "*" and line[i + 1] == "/":
                    in_block = False
                    i += 2
                elif in_block:
                    i += 1
                elif i + 1 < n and line[i] == "/" and line[i + 1] == "/":
                    break
                elif not in_block:
                    cleaned += line[i]
                    i += 1
            if cleaned and not in_block: 
                code.append(cleaned)
                cleaned = ""
        return code