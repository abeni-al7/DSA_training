class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targind = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                targind.append(i)
        return targind
