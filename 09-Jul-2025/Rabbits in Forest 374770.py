# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        colors = defaultdict(int)
        for answer in answers:
            colors[answer] += 1
        
        count = 0
        for k, v in colors.items():
            size = k + 1
            groups = (v + size - 1) // size
            count += groups * size
        return count