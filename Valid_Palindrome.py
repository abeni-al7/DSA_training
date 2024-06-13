class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if char.isalnum():
                new_str += char
        new_str = new_str.lower()
        l, r = 0, len(new_str) - 1
        while l < r:
            if new_str[r] != new_str[l]:
                return False
            l += 1
            r -= 1
        return True
        
