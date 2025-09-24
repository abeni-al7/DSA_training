# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = deque([(0, -1)])
        current_sum = 0
        min_len = float('inf')

        for i in range(len(nums)):
            current_sum += nums[i]
            while prefix and current_sum - prefix[0][0] >= k:
                min_len = min(min_len, i - prefix[0][1])
                prefix.popleft()
            
            while prefix and current_sum < prefix[-1][0]:
                prefix.pop()
            prefix.append((current_sum, i))
        
        return min_len if min_len != float('inf') else -1
            