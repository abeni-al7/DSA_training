# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_count = defaultdict(int)
        winners = set()
        answer = [[], []]

        for match in matches:
            winners.add(match[0])
            lose_count[match[1]] += 1

        for k, v in lose_count.items():
            if v == 1:
                answer[1].append(k)
        answer[1].sort()

        for winner in winners:
            if winner not in lose_count:
                answer[0].append(winner)
        answer[0].sort()
              
        return answer  