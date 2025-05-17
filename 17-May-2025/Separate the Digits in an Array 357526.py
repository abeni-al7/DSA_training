# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            digits = []
            while num:
                digits.append(num % 10)
                num //= 10
            digits.reverse()
            answer.extend(digits)
        return answer
        