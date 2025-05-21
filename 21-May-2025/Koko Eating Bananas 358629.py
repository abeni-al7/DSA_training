# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k):
            time = 0
            for pile in piles:
                if pile <= k:
                    time += 1
                else:
                    time += ceil(pile / k)
            return time <= h

        left, right = 1, max(piles)
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if can_eat(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans