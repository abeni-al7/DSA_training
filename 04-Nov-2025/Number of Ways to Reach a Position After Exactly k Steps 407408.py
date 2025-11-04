# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def fact(self, num):
        MOD = 10**9 + 7
        fact = [-1] * (num + 1)
        fact[0] = 1
        for i in range(1, num+1):
            fact[i] = (fact[i-1] * i) % MOD
        return fact[num]

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        d = abs(endPos - startPos)
        if (k + d) % 2 or (k - d) % 2 or (k + d) < 0 or (k - d) < 0:
            return 0
        
        r = (k + d) // 2
        l = (k - d) // 2

        denom = (self.fact(r) * self.fact(l)) % MOD
        denom_inv = pow(denom, MOD-2, MOD)

        return (self.fact(k) * denom_inv) % MOD