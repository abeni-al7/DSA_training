# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None 
        tortoise = head
        rabbit = head
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
            if tortoise == rabbit:
                break
        
        tortoise = head
        if rabbit == tortoise:
            return head
        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next
            if tortoise == rabbit:
                return rabbit
        return None