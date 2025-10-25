# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        bitmask = 0
        ans = []

        for i in range(2 ** len(nums)):
            curr = []
            for j in range(32):
                if bitmask & (1 << j):
                    curr.append(nums[len(nums) - j - 1])
            ans.append(curr)
            bitmask += 1
        return ans