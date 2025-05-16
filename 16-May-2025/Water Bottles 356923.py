# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = 0
        empty = 0
        current = numBottles

        while current:
            empty += current
            drank += current
            current = empty // numExchange
            empty %= numExchange
        
        return drank