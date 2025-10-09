# Problem: Number of Subarrays With GCD Equal to K - https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/description/

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if a % b == 0:
                return b
            return gcd(b, a % b)
        
        count = 0
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr = gcd(curr, nums[j])
                if curr == k:
                    count += 1
                elif curr < k:
                    break
        return count
