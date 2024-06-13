class Solution:
    def nextIndex(self, nums, index, forward):
        direction = nums[index] >= 0
        if direction != forward:
            return -1
        next_index = (index + nums[index]) % len(nums)
        if next_index < 0:
            next_index += len(nums)
        if next_index == index:
            return -1
        return next_index

    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        for i in range(len(nums)):
            slow, fast = i, i
            forward = nums[i] > 0
            while True:
                slow = self.nextIndex(nums, slow, forward)
                if slow == -1:
                    break
                fast = self.nextIndex(nums, fast, forward)
                if fast == -1:
                    break
                fast = self.nextIndex(nums, fast, forward)
                if fast == -1:
                    break
                if slow == fast:
                    return True
        return False
        
