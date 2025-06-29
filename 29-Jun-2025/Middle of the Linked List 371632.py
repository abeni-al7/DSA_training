# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        size = 0
        current = dummy
        while current.next:
            current = current.next
            size += 1
        
        index = size // 2
        current = dummy.next
        for _ in range(index):
            current = current.next
        return current