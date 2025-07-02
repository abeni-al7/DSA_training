# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)
        left_tail = left_dummy
        right_tail = right_dummy

        current = head
        while current:
            if current.val < x:
                left_tail.next = current
                left_tail = left_tail.next
            else:
                right_tail.next = current
                right_tail = right_tail.next
            current = current.next
        
        left_tail.next = right_dummy.next
        right_tail.next = None

        return left_dummy.next