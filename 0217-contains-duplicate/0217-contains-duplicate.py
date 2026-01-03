class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False
        
"""
nums = [1, 2, 3, 4]
              i
                 j
Time: O(n^2)
Space: O(1)

hashset = {1, 2, 3, 4}

Time: O(n)
Space: O(n)
"""