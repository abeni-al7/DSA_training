# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        answer = []
        first = (num - 3) // 3
        if 3 * first + 3 == num:
            answer.append(first)
            answer.append(first + 1)
            answer.append(first + 2)
        return answer
        