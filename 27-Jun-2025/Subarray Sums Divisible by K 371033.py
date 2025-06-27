# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_remainder = defaultdict(int)
        prefix_remainder[0] = 1
        current_sum = 0
        count = 0
    
        for num in nums:
            current_sum += num
            remainder = (current_sum % k + k) % k
            count += prefix_remainder[remainder]
            prefix_remainder[remainder] += 1
        return count
