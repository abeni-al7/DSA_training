# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        # code here
        memo = [[0 for j in range(W + 1)] for i in range(len(val) + 1)]
        
        for i in range(1, len(val) + 1):
            for j in range(1, W + 1):
                if j - wt[i-1] >= 0:
                    memo[i][j] = max(
                        memo[i-1][j], 
                        memo[i-1][j-wt[i-1]] + val[i-1]
                    )
                else:
                    memo[i][j] = memo[i-1][j]
        return memo[-1][-1]
