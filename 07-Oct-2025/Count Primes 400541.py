# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        d = 2
        primes = []
        eliminated = set()
        while d < n:
            if d not in eliminated:
                primes.append(d)
                j = d * d
                while j < n:
                    eliminated.add(j)
                    j += d
            d += 1
        return len(primes)