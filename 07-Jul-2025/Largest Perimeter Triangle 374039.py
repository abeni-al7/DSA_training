# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        s1, s2, s3 = len(nums) - 1, len(nums) - 2, len(nums) - 3
        max_perimeter = 0
        while s3 >= 0:
            current_perimeter = nums[s1] + nums[s2] + nums[s3]
            if nums[s2] + nums[s3] > nums[s1]:
                max_perimeter = max(max_perimeter, current_perimeter)
            s1 -= 1
            s2 -= 1
            s3 -= 1
        return max_perimeter