# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")
        cur_sum = 0
        q = deque() # pref, end_idx

        for r in range(len(nums)):
            cur_sum += nums[r]
            if cur_sum >= k:
                res = min(res, r + 1)
            
            while q and cur_sum - q[0][0] >= k:
                prefix, end_idx = q.popleft()
                res = min(res, r - end_idx)
            
            while q and q[-1][0] >= cur_sum:
                q.pop()
            q.append((cur_sum, r))

        return res if res != float("inf") else -1