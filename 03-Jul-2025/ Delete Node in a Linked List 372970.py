# Problem:  Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        current = node.next
        while current.next:
            prev.val = current.val
            prev = prev.next
            current = current.next
        prev.val = current.val
        prev.next = None
        