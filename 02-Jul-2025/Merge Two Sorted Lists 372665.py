# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode(0)
        current = merged
        while list1 and list2:
            if list1.val <= list2.val:
                new_val = list1.val
                new_node = ListNode(new_val)
                current.next = new_node
                list1 = list1.next
            else:
                new_val = list2.val
                new_node = ListNode(new_val)
                current.next = new_node
                list2 = list2.next
            current = current.next
        
        while list1:
            new_val = list1.val
            new_node = ListNode(new_val)
            current.next = new_node
            list1 = list1.next
            current = current.next
        
        while list2:
            new_val = list2.val
            new_node = ListNode(new_val)
            current.next = new_node
            list2 = list2.next
            current = current.next
            
        return merged.next

        