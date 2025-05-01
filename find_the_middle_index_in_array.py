class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = []
        rightSum = []
        l, r = 0, 0
        for i in range(len(nums)):
            leftSum.append(l)
            l += nums[i]
        for i in range(len(nums) - 1, -1, -1):
            rightSum.append(r)
            r += nums[i]
        rightSum.reverse()
        for i in range(len(nums)):
            if leftSum[i] == rightSum[i]:
                return i
        return -1
