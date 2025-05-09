# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        write = 0
        for read in range(n):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        
        for i in range(write, n):
            nums[i] = 0