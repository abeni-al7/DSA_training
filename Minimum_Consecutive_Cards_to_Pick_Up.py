class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        lastIndex = defaultdict(lambda: -1)
        minLength = float('inf')
        for i in range(len(cards)):
            if lastIndex[cards[i]] != -1:
                minLength = min(i - lastIndex[cards[i]] + 1, minLength)
            lastIndex[cards[i]] = i
        return -1 if minLength == float('inf') else minLength
            
