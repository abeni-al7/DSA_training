# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = deque([root])
        output = []
        while queue:
            result = []
            for _ in range(len(queue)):
                node = queue.popleft()
                result.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            output.append(result)
        return output