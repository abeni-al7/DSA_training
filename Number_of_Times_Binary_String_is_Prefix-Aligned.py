class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_seen = 0

        for i, flip in enumerate(flips):
            max_seen = max(max_seen, flip)
            if max_seen == i + 1:
                count += 1

        return count
