# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [0] * (target + 1)

        for i in range(len(memo)):
            if i == 0:
                memo[i] = 1
            else:
                result = 0
                for num in nums:
                    result += memo[i - num] if i - num >= 0 else 0
                memo[i] = result
        return memo[target]