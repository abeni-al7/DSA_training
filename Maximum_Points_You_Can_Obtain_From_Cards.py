class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        current = sum(cardPoints[r:])
        maxScore = current
        while r < len(cardPoints):
            current += (cardPoints[l] - cardPoints[r])
            l += 1
            r += 1
            maxScore = max(maxScore, current)
        return maxScore
