# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        cur_avg = cur_sum / k
        max_avg = cur_avg
        l = 0
        for r in range(k, len(nums)):
            cur_sum -= nums[l]
            cur_sum += nums[r]
            cur_avg = cur_sum / k
            max_avg = max(max_avg, cur_avg)
            l += 1
        return max_avg