# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = [0] * len(questions)

        for i in range(len(questions) - 1, -1, -1):
            next_i = i + questions[i][1] + 1
            choose = questions[i][0] + (memo[next_i] if next_i < len(questions) else 0)
            skip = memo[i+1] if i+1 < len(questions) else 0
            memo[i] = max(choose, skip)
        return memo[0]