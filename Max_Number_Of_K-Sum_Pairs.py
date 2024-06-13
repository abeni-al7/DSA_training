class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total < k:
                l += 1
            elif total > k:
                r -= 1
            else:
                count += 1
                l += 1
                r -= 1
        return count

        
