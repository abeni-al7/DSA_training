# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                num -= 1
            elif i + 1 < len(s) and s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                num -= 10
            elif i + 1 < len(s) and s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                num -= 100
            else:
                num += dictionary[s[i]]
        return num