# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode()
        dummy.next = head
        current = dummy
        while current.next and current.next.val < x:
            current = current.next
        
        prev = current
        seeker = current.next
        while seeker:
            if seeker.val < x:
                prev.next = seeker.next
                seeker.next = current.next
                current.next = seeker
                current = current.next
            else:
                prev = prev.next
            seeker = prev.next
        return dummy.next