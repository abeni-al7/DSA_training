# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(left, right):
            if left and right and left.val == right.val:
                if not (symmetric(left.left, right.right) and symmetric(left.right, right.left)):
                    return False
            if left and not right or right and not left:
                return False
            if left and right and left.val != right.val:
                return False
            return True
        return symmetric(root.left, root.right)       