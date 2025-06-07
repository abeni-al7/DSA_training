# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        answer = [0] * 2
        for val in freq.values():
            if val % 2 != 0:
                answer[1] += 1
            answer[0] += val // 2
        return answer