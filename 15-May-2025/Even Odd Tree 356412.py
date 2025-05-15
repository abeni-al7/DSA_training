# Problem: Even Odd Tree - https://leetcode.com/problems/even-odd-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        queue = deque([root])
        while queue:
            current = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if current and node.val <= current[-1]:
                            return False
                else:
                    if node.val % 2:
                        return False
                    if current and node.val >= current[-1]:
                        return False
                current.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level += 1
        return True