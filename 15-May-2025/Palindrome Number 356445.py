# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = []
        while x:
            num.append(x % 10)
            x //= 10
        l, r = 0, len(num) - 1
        while l < r:
            if num[l] != num[r]:
                return False
            l += 1
            r -= 1
        return True