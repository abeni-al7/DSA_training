class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        heap = []
        for i, num in enumerate(arr):
            heapq.heappush(heap, (num, i))
        
        res = [0] * len(arr)
        rank = 0
        prev = -1
        while heap:
            curr, idx = heapq.heappop(heap)
            if prev < 0 or arr[prev] != arr[idx]:
                rank += 1
            res[idx] = rank
            prev = idx
        return res