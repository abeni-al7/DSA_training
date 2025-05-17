# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = time % (2 * (n - 1))
        if cycle < n:
            return cycle + 1
        else:
            return n - (cycle - (n - 1))