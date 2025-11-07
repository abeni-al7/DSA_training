# Problem: Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        if remainder == 0:
            return 0

        current = 0
        last_remain = {0: -1}
        min_len = len(nums)
        for i, num in enumerate(nums):
            current = (current + num) % p
            prefix = (current - remainder + p) % p
            if prefix in last_remain:
                min_len = min(min_len, i - last_remain[prefix])
            last_remain[current] = i
        return min_len if min_len != len(nums) else -1