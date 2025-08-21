# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        current = target
        doubles = maxDoubles
        count = 0

        while current > 1 and doubles > 0:
            if current % 2 == 1:
                current -= 1
            else:
                doubles -= 1
                current //= 2
            count += 1

        count += current - 1
        
        return count