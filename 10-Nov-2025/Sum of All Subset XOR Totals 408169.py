# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        memo = {}
        def backtrack(i, curr):
            if i == len(nums):
                return curr
            if (i, curr) in memo:
                return memo[(i, curr)]

            memo[(i, curr)] = backtrack(i + 1, curr ^ nums[i]) + backtrack(i + 1, curr)
            return memo[(i, curr)]
        return backtrack(0, 0)