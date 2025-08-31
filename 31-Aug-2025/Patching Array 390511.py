# Problem: Patching Array - https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        current_max = 0
        count = 0
        i = 0
        while i < len(nums) and current_max < n: 
            if nums[i] <= current_max + 1:
                current_max += nums[i]
                i += 1
            else:
                count += 1
                current_max += (current_max + 1)

        while current_max < n:
            count += 1
            current_max += (current_max + 1)
            
        return count
        
        