# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered  = set()
        for interval in ranges:
            for i in range(interval[0], interval[1] + 1):
                covered.add(i)
        for i in range(left, right+1):
            if i not in covered:
                return False
        return True