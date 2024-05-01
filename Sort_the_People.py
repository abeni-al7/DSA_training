class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for i in range(len(heights)):
            j = i
            while heights[j] > heights[j - 1] and j > 0:
                heights[j], heights[j - 1] = heights[j - 1], heights[j]
                names[j], names[j - 1] = names[j - 1], names[j]
                j -= 1
                
        return names
