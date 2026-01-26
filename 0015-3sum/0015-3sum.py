class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        visited = set()
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                current = nums[l] + nums[r]
                if current == target and (nums[i], nums[l], nums[r]) not in visited:
                    triplets.append([nums[i], nums[l], nums[r]])
                    visited.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif current < target:
                    l += 1
                else:
                    r -= 1
        return triplets
            
"""
visited = 
nums = [-4, -1, -1, 0, 1, 2]
             l         r
"""