# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        total = len(nums)
        freq = Counter(nums)
        pairs = sum(count // 2 for count in freq.values())
        return [pairs, total - 2 * pairs]