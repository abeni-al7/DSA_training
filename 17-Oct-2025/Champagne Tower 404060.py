# Problem: Champagne Tower - https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured]

        for i in range(1, query_row + 1):
            curr = [0] * (i + 1)
            for j in range(i):
                extra = prev_row[j] - 1
                if extra > 0:
                    curr[j] += 0.5 * extra
                    curr[j + 1] += 0.5 * extra
            prev_row = curr
        
        return min(1, prev_row[query_glass])
        