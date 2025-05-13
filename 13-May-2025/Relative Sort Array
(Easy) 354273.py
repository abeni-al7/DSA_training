# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

from collections import Counter
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []

        # Add elements in arr2 order
        for num in arr2:
            result.extend([num] * count.pop(num))

        # Add remaining elements in sorted order
        for num in sorted(count.keys()):
            result.extend([num] * count[num])

        return result
