class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0] + nums[1] + nums[len(nums)-1]
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                current = nums[i] + nums[l] + nums[r]
                if current > target:
                    r -= 1
                else:
                    l += 1
                if abs(current - target) < abs(closest - target):
                    closest = current
        return closest

        
