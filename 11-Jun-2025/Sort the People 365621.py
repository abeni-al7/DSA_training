# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            max_index = i
            for j in range(i + 1, len(names)):
                if heights[j] > heights[max_index]:
                    max_index = j
            names[i], names[max_index] = names[max_index], names[i]
            heights[i], heights[max_index] = heights[max_index], heights[i]

        return names
        