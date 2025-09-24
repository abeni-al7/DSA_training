# Problem: Car fleet - https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            stack.append([position[i], time])
        
        stack.sort()
        fleets = 1
        while stack:
            top = stack.pop()
            if stack and top[1] < stack[-1][1]:
                fleets += 1
            elif stack:
                stack[-1][1] = top[1]
        return fleets
