# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = [[0 for _ in range(2)] for _ in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):
            for j in range(2):
                if j == 1:
                    memo[i][j] = max(
                        -prices[i] + memo[i+1][0], 
                        memo[i+1][1]
                    )
                else:
                    memo[i][j] = max(
                        prices[i] - fee + memo[i+1][1],
                        memo[i+1][0]
                    )

        return memo[0][1]
        