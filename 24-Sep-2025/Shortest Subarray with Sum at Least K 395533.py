# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Build prefix sum array
        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])

        # initialize monotonically increasing queue and result
        dq = deque()
        res = float('inf')

        for i in range(len(prefix)):
            # Pop from the front and calculate valid length of subarray
            while dq and prefix[i] - prefix[dq[0]] >= k:
                res = min(res, i - dq.popleft())
            
            # Pop from the back to maintain monotonic increasing order
            while dq and prefix[i] < prefix[dq[-1]]:
                dq.pop()

            dq.append(i)
        
        return res if res != float('inf') else -1
            