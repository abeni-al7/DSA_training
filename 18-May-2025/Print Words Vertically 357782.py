# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        vertical = [""] * max(len(w) for w in s)

        for i in range(len(vertical)):
            for j in range(len(s)):
                if i < len(s[j]):
                    vertical[i] += s[j][i]
                else:
                    vertical[i] += " "
            vertical[i] = vertical[i].rstrip()
        return vertical