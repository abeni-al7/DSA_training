# Problem: Smallest Range Covering Elements from K Lists - https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        left = right = nums[0][0]
        min_heap = []
        for i in range(k):
            l = nums[i]
            left = min(left, l[0])
            right = max(right, l[0])
            heapq.heappush(min_heap, (l[0], i, 0)) # n, index of list, index of n
        
        res = [left, right]
        while True:
            n, i, idx = heapq.heappop(min_heap)
            idx += 1
            if idx == len(nums[i]):
                return res
            
            next_val = nums[i][idx]
            heapq.heappush(min_heap, (next_val, i, idx))
            left = min_heap[0][0]
            right = max(right, next_val)
            if right - left < res[1] - res[0]:
                res = [left, right]