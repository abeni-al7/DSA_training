# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)

        def gcd(a, b):
            if a % b == 0:
                return b
            return gcd(b, a % b)
        
        return gcd(large, small)