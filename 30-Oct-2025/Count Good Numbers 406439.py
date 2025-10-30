# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def power(self, base, x):
        res = 1
        while x > 0:
            if x & 1:
                res = (res * base) % (10**9 + 7)
            base = (base * base) % (10**9 + 7)
            x >>= 1
        return res

    def countGoodNumbers(self, n: int) -> int:
        even = math.ceil(n / 2)
        odd = n // 2
        ans = (self.power(5, even) * self.power(4, odd)) % (10**9 + 7)
        return ans