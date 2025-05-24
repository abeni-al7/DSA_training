# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = {}
        min_sum = float("inf")

        for i in range(len(list1)):
            if list1[i] in list2:
                common[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in common:
                common[list2[j]] += j
                min_sum = min(min_sum, common[list2[j]])
        
        output = []
        for key in common:
            if common[key] == min_sum:
                output.append(key)
        return output