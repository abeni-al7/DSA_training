# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] # [temp, 1, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                last = stack.pop()
                if stack:
                    stack[-1][1] += last[1]
                answer[last[2]] = last[1]
            stack.append([temp, 1, i])
        return answer
