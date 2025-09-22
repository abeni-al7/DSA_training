# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def __init__(self):
        self.count = 0
        self.memo = [0] * 46
        self.memo[1] = 1
        self.memo[2] = 2

    def climbStairs(self, n: int) -> int:
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]
        
