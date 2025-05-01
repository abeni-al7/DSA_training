# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if (root != None):
            output.append(root.val)
            output.extend(self.preorderTraversal(root.left))
            output.extend(self.preorderTraversal(root.right))
        return output
