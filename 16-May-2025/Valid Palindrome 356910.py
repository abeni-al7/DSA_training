# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        if s == "":
            return True
        formatted = ""
        for char in s:
            if char in alphabet:
                formatted += char.lower()
        l, r = 0, len(formatted) - 1
        while l < r:
            if formatted[l] != formatted[r]:
                return False
            l += 1
            r -= 1
        return True