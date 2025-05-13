# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        maximum = max(arr1)
        count = [0] * (maximum + 1)
        for val in arr1:
            count[val] += 1
        
        answer = []
        for val in arr2:
            count[val]
            while count[val] > 0:
                answer.append(val)
                count[val] -= 1
        
        for i in range(len(count)):
            while count[i]:
                answer.append(i)
                count[i] -= 1
        return answer