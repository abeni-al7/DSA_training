class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        for i in range(len(ranges)):
            value = ranges[i][0]
            while value <= ranges[i][1]:
                covered.add(value)
                value += 1
        for i in range(left, right + 1):
            if i not in covered:
                return False
        return True
