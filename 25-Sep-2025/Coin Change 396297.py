# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(amount):
            if amount == 0:
                return 0
            if amount in coins:
                return 1
            if amount not in memo:
                possible = [float('inf')]
                for coin in coins:
                    if amount - coin >= 0:
                        possible.append(dp(amount - coin) + 1)
                memo[amount] = min(possible)
            return memo[amount]
           
        min_coins = dp(amount)

        return min_coins if min_coins != float('inf') else -1