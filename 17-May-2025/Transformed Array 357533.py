# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            if nums[i] > 0:
                idx = (i + nums[i]) % n
                print(idx, n, i)
                result.append(nums[idx])
            elif nums[i] < 0:
                idx = (i - abs(nums[i])) % n
                result.append(nums[idx])
            else:
                result.append(nums[i])
        return result