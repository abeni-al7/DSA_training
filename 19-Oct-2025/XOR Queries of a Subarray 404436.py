# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(arr))
        curr = 0
        for i in range(len(arr)):
            curr ^= arr[i]
            prefix[i] = curr
        
        answer = []
        for q in queries:
            l, r = q
            if r == l:
                answer.append(arr[l])
            elif l == 0:
                answer.append(prefix[r])
            else:
                val = prefix[r] ^ prefix[l - 1]
                answer.append(val)
        return answer
