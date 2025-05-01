class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        remainder_count = defaultdict(int)
        remainder_count[0] = 1
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            count += remainder_count[remainder]
            remainder_count[remainder] += 1
        return count

