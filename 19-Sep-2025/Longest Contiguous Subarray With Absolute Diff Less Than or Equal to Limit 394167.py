# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = deque()
        min_queue = deque()

        max_len = 0
        l = 0
        for r in range(len(nums)):
            while max_queue and nums[r] > max_queue[-1]:
                max_queue.pop()
            while min_queue and nums[r] < min_queue[-1]:
                min_queue.pop()
            
            max_queue.append(nums[r])
            min_queue.append(nums[r])

            while max_queue[0] - min_queue[0] > limit:
                if nums[l] == max_queue[0]:
                    max_queue.popleft()
                if nums[l] == min_queue[0]:
                    min_queue.popleft()
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len