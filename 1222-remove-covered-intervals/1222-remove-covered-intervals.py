class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        cleaned = []

        for i in intervals:
            if cleaned and cleaned[-1][0] <= i[0] and i[1] <= cleaned[-1][1]:
                continue
            cleaned.append(i)
        
        return len(cleaned)