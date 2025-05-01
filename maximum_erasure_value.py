class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited = {}
        current, score = 0, 0
        l = 0
        for r, num in enumerate(nums):
            if num in visited:
                while l < visited[num] + 1:
                    current -= nums[l]
                    l += 1
            visited[num] = r
            current += nums[r]
            score = max(score, current)
        return score
