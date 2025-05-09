# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [x for x in range(1, n + 1)]
        i = 0
        while len(players) > 1:
            count = 0
            while count < k - 1:
                i = (i + 1) % len(players)
                count += 1
            players.pop(i)
        return players[0]
                
