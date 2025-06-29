# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next != None:
            current = current.next
            size += 1
        
        index = size - n
        prev = dummy
        current = head
        i = 0
        while i < index:
            prev = current
            current = current.next
            i += 1
        prev.next = current.next
        return dummy.next