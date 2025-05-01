from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def findMax(root, minimum, maximum):
            if not root:
                return -1
            minimum = min(minimum, root.val)
            maximum = max(maximum, root.val)

            left = findMax(root.left, minimum, maximum)
            right = findMax(root.right, minimum, maximum)

            return max((maximum - minimum), max(left, right))
        return findMax(root, float(inf), float(-inf))