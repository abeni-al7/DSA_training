# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        maximums = []
        current = float(-inf)
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                current = max(current, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            maximums.append(current)
            current = float(-inf)
        return maximums
