# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        x = target
        doubles = maxDoubles
        while x > 1 and doubles:
            if x % 2:
                x -= 1
                count += 1
            x //= 2
            count += 1
            doubles -= 1
        count += x - 1
        return count