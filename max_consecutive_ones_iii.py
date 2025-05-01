class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k >= len(nums):
            return len(nums)
        window = Counter(nums[:k])
        answer = 0
        l = 0
        for r in range(k, len(nums)):
            if nums[r] == 1:
                if window[1]:
                    window[1] += 1
                else:
                    window[1] = 1
            elif window[0] < k:
                if window[0]:
                    window[0] += 1
                else:
                    window[0] = 1
            else:
                while nums[l] == 1:
                    l += 1
                l += 1
            answer = max(answer, r - l + 1)
        return answer
        
