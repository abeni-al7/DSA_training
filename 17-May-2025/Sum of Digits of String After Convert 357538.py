# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digits = ""
        for char in s:
            digits += str(ord(char) - ord("a") + 1)
        digits = int(digits)

        num = 0
        while k:
            while digits:
                num += (digits % 10)
                digits //= 10
            k -= 1
            digits = num
            num = 0
        
        return digits