# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                pieces = math.ceil(nums[i] / nums[i + 1])
                largest = math.floor(nums[i] / pieces)
                count += pieces - 1
                nums[i] = largest
        return count
            