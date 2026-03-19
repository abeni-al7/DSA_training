class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for i in range(len(nums2) - 1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            if stack:
                next_greater[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        
        output = []
        for num in nums1:
            output.append(next_greater.get(num, -1))
        return output
"""
nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
expected = [7,7,7,7,7]
next = {1: 7, 2: 7}
stack = [7, 3]
"""
            