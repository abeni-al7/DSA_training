# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            minimum = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] < minimum:
                    minimum = nums[j]
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

        