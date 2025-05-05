# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = []
        if x < 0:
            return False
        while x:
            nums.append(x % 10)
            x //= 10
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True
        