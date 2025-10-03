# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dp(node):
            if node == None:
                return 0
            
            if node in memo:
                return memo[node]
            
            left_left = left_right = right_left = right_right = None
            if node.left:
                left_left = node.left.left
                left_right = node.left.right
            if node.right:
                right_left = node.right.left
                right_right = node.right.right

            memo[node] = max(
                node.val + dp(left_left) + dp(left_right) + dp(right_left) + dp(right_right),
                dp(node.left) + dp(node.right)
            )
            return memo[node]
        return dp(root)