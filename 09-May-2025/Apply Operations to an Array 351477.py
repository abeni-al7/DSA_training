# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] *= 2
                nums[right] = 0
            left += 1
            right += 1
        
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1
        return nums