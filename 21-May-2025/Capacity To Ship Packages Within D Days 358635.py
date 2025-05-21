# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            total = 1
            curr = 0
            for weight in weights:
                if curr + weight > capacity:
                    curr = weight
                    total += 1
                else:
                    curr += weight
            return total <= days

        left, right = max(weights), sum(weights)
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if can_ship(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans