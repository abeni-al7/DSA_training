class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        xpart = []
        for i in range(len(points)):
            xpart.append(points[i][0])
        xpart.sort()
        maxDifference = 0
        for i in range(len(xpart)):
            if i == 0:
                continue
            diff = xpart[i] - xpart[i - 1]
            if diff > maxDifference:
                maxDifference = diff
        return maxDifference
