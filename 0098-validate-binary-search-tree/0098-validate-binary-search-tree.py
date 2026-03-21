# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = []
        def preorder(node):
            if node.left:
                preorder(node.left)
            nums.append(node.val)
            if node.right:
                preorder(node.right)
        preorder(root)

        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True
            