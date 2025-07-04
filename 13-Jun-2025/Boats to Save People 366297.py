# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1

        result = 0
        while l <= r:
            if l != r and people[l] + people[r] <= limit:
                l += 1
                r -= 1
                result += 1
            else:
                r -= 1
                result += 1
        return result