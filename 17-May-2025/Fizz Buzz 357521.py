# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            result = ""
            if i % 3 == 0:
                result += "Fizz"
            if i % 5 == 0:
                result += "Buzz"
            answer.append(result or str(i))
        return answer