# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        max_score = count[1]
        current = count[1]
        score = defaultdict(list)
        score[current].append(0)
        for i in range(1, len(nums)):
            if nums[i - 1] == 1:
                current -= 1
            else:
                current += 1
            score[current].append(i)
            max_score = max(max_score, current)

        if nums[-1] == 1:
            current -= 1
        else:
            current += 1
        score[current].append(len(nums))
        max_score = max(max_score, current)
        return score[max_score]