# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        second = {}
        for i, first in enumerate(nums):
            second[target - first] = i

        for i, num in enumerate(nums):
            if num in second and i != second[num]:
                return [i, second[num]]