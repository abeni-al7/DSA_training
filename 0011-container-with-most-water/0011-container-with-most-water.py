class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            current = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
"""
height = [1,8,6,2,5,4,8,3,7]
                    l r
max_area = 49
curr = 4
"""