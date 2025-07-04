# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pal = []
        while head:
            pal.append(head.val)
            head = head.next
        l, r = 0, len(pal) - 1
        while l <= r:
            if pal[l] != pal[r]:
                return False
            l += 1
            r -= 1
        return True