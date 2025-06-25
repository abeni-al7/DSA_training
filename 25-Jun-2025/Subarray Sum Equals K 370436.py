# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        current = 0
        count = 0
        for i, num in enumerate(nums):
            current += num
            target = current - k
            count += prefix[target]
            prefix[current] += 1
        return count