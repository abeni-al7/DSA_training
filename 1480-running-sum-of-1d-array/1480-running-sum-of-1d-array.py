class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        current = 0
        for num in nums:
            current += num
            prefix.append(current)
        return prefix
