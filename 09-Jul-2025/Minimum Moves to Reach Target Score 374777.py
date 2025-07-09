# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        if target % 2 != 0:
            target -= 1
            count += 1
    
        while target > 1 and maxDoubles > 0:
            target //= 2
            if target % 2:
                target -= 1
                count += 1
            count += 1
            maxDoubles -= 1
        
        count += target - 1
        return count