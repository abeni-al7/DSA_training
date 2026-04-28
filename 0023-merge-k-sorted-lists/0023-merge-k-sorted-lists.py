# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        dummy = ListNode(0)
        current = dummy
        counter = 0

        for l in lists:
            if l:
                heapq.heappush(minHeap, (l.val, counter, l))
                counter += 1

        while minHeap:
            val, _, node = heapq.heappop(minHeap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, counter, node.next))
                counter += 1
        return dummy.next
