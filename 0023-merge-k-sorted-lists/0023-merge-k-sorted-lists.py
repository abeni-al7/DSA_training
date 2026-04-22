# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for l in lists:
            current = l
            while current:
                heapq.heappush(minHeap, current.val)
                current = current.next
        
        if not minHeap:
            return None

        root = ListNode(heapq.heappop(minHeap))
        current = root
        while minHeap:
            current.next = ListNode(heapq.heappop(minHeap))
            current = current.next
        
        return root
