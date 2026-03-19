class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                answer[i] = stack[-1][1] - i
            stack.append([temperatures[i], i])
        return answer

"""
temperatures = [73,74,75,71,69,72,76,73]

warmer = [1,1,4,2,1,1,0,0]
stack = [(76, 6), (75, 2), (74, 1), (73, 0)]
"""