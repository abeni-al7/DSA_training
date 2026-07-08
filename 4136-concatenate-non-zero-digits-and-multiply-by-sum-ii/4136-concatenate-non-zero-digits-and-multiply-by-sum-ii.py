MOD = 10**9 + 7
pow10 = [1] * 1000001
for i in range(1, 1000001):
    pow10[i] = pow10[i - 1] * 10 % MOD

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        x_prefix = [0] * (n + 1)
        sum_prefix = [0] * (n + 1)
        count_prefix = [0] * (n + 1)

        for i, char in enumerate(s):
            num = int(char)
            sum_prefix[i + 1] = sum_prefix[i] + num
            x_prefix[i + 1] = (x_prefix[i] * 10 + num) % MOD if num > 0 else x_prefix[i]
            count_prefix[i + 1] = count_prefix[i] + (num > 0)
        
        answer = []
        for l, r in queries:
            length = count_prefix[r + 1] - count_prefix[l]
            x = x_prefix[r + 1] - x_prefix[l] * pow10[length]
            s = sum_prefix[r + 1] - sum_prefix[l]
            ans = (x * s) % MOD
            answer.append(ans)

        return answer
