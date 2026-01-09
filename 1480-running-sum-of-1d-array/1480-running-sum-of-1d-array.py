class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        for i in range(len(nums)):
            current = 0
            for j in range(i + 1):
                current += nums[j]
            running_sum.append(current)
        return running_sum
