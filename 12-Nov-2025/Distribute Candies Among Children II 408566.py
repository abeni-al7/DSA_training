# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def comb2(self, x: int) -> int:
        if x < 0:
            return 0
        return x * (x - 1) // 2

    def distributeCandies(self, n: int, limit: int) -> int:
        total = self.comb2(n + 2)
        sub1 = 3 * self.comb2((n + 2) - (limit + 1))
        add1 = 3 * self.comb2((n + 2) - 2*(limit + 1))
        sub2 = self.comb2((n + 2) - 3*(limit+1))
        return total - sub1 + add1 - sub2