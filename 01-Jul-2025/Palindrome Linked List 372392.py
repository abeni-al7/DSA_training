# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow.next
        prev = None
        curr = middle
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        first, second = head, prev
        result = False
        while first and second and first.val == second.val:
            first = first.next
            second = second.next
            result = True
            if first and second and first.val != second.val:
                return False
        return result