# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0

        device_per_row = []
        for row in bank:
            ones = 0
            for val in row:
                if val == "1":
                    ones += 1
            device_per_row.append(ones)

        curr = 0
        if all(x == 0 for x in device_per_row):
            return 0
        for i in range(len(device_per_row)):
            if device_per_row[i] == 0:
                continue
            if curr == 0:
                curr = device_per_row[i]
                continue
            curr *= device_per_row[i]
            count += curr
            curr = device_per_row[i]
            
        return count