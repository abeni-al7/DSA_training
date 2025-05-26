# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(x for x in nums if x % 2 == 0)
        result = []

        for value_to_add, idx in queries:
            current = nums[idx]
            was_even = current % 2 == 0

            if was_even:
                even_sum -= current

            nums[idx] += value_to_add
            updated = nums[idx]

            if updated % 2 == 0:
                even_sum += updated
                
            result.append(even_sum)

        return result