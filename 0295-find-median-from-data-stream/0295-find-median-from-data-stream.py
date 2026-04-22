class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.bigHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.smallHeap, num)
        if len(self.smallHeap) > len(self.bigHeap) + 1:
            heapq.heappush(self.bigHeap, heapq.heappop_max(self.smallHeap))
        
        if self.smallHeap and self.bigHeap and self.smallHeap[0] > self.bigHeap[0]:
            heapq.heappush(self.bigHeap, heapq.heappop_max(self.smallHeap))
        
        if len(self.bigHeap) > len(self.smallHeap) + 1:
            heapq.heappush_max(self.smallHeap, heapq.heappop(self.bigHeap))

    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.bigHeap):
            return (self.smallHeap[0] + self.bigHeap[0]) / 2
        elif len(self.smallHeap) > len(self.bigHeap):
            return self.smallHeap[0]
        return self.bigHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()