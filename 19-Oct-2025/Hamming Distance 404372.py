# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        xor = x ^ y
        while xor:
            if xor & 1:
                count += 1
            xor >>= 1
        return count
        