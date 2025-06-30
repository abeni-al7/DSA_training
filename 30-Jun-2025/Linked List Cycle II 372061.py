# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = rabbit = head
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            if tortoise == rabbit:
                tortoise = head
                while tortoise != rabbit:
                    tortoise = tortoise.next
                    rabbit = rabbit.next
                return tortoise
        return None