# Problem: Decode XORed Array - https://leetcode.com/problems/decode-xored-array/description/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        answer = [first]
        for i in range(len(encoded)):
            after = answer[i] ^ encoded[i]
            answer.append(after)
        return answer