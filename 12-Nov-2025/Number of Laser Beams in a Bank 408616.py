# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        prev = bank[0].count("1")

        for i in range(1, len(bank)):
            curr = bank[i].count("1")
            if curr:
                count += prev * curr
                prev = curr
        
        return count