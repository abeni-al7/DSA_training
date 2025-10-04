# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, buy):
            if i >= len(prices):
                return 0
            
            if (i, buy) in memo:
                return memo[(i, buy)]

            if buy:
                memo[(i, buy)] = max(
                    -prices[i] + dp(i+1, 0), 
                    dp(i+1, 1)
                )
            else:
                memo[(i, buy)] = max(
                    prices[i] + dp(i+2, 1), 
                    dp(i+1, 0)
                )
            return memo[(i, buy)]
        return dp(0, 1)
        