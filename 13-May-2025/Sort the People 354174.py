# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if heights[j] < heights[j + 1]:  # Descending
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
                    swapped = True
            if not swapped:
                break  # Optimization: stop if already sorted
        return names
