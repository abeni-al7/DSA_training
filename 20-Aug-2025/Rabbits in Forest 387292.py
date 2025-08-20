# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = 0
        freq = Counter(answers)

        for k, v in freq.items():
            groups = math.ceil(v / (k + 1))
            count += groups * (k + 1)
                    
                
        return count