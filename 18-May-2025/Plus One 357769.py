# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, (str(int("".join(str(d) for d in digits)) + 1))))