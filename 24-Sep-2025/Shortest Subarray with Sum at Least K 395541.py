# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # Build prefix sum array
        prefix = [0]
        for num in nums:
            prefix.append(num + prefix[-1])

        # monoq stores indices of prefix sums in increasing order
        monoq = deque()
        answer = float('inf')

        for i in range(len(prefix)):
            # Pop from the front and calculate valid length of subarray
            while monoq and prefix[i] - prefix[monoq[0]] >= k:
                answer = min(answer, i - monoq.popleft())
            
            # Pop from the back to maintain monotonic increasing order
            while monoq and prefix[i] <= prefix[monoq[-1]]:
                monoq.pop()

            monoq.append(i)
        
        return answer if answer != float('inf') else -1
            