# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        colors = defaultdict(int)
        count = 0

        for answer in answers:
            if colors[answer] == answer:
                count += answer + 1
                del colors[answer]
            else:
                colors[answer] += 1
                
        count += sum(key + 1 for key in colors.keys())

        return count



            