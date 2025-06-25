# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for shift in shifts:
            l, r, d = shift
            if d == 0:
                diff[l] -= 1
                diff[r + 1] += 1
            else:
                diff[l] += 1
                diff[r + 1] -= 1

        current = 0
        prefix = []
        for i in range(len(s)):
            current += diff[i]
            prefix.append(current) 
        
        output = ""
        for i, char in enumerate(s):
            val = ord(char) - ord("a")
            val = (val + prefix[i]) % 26
            new_char = chr(ord("a") + val)
            output += new_char
        return output