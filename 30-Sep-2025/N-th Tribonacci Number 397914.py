# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return n
        
        if n == 1 or n == 2:
            return 1
        
        ans = [0] * (n + 1)
        ans[1] = ans[2] = 1

        for i in range(3, n + 1):
            ans[i] = ans[i-1] + ans[i-2] + ans[i-3]

        return ans[-1]