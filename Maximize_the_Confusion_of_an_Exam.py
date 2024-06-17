class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answer = 0
        helper_map = {'T': 0, 'F': 0}
        l = 0
        for r in range(len(answerKey)):
            helper_map[answerKey[r]] += 1
            allowed = min(helper_map['T'], helper_map['F'])
            if allowed > k:
                while min(helper_map['T'], helper_map['F']) > k:
                    helper_map[answerKey[l]] -= 1
                    if helper_map[answerKey[l]] < 0:
                        helper_map[answerKey[l]] = 0
                    l += 1
            answer = max(answer, r-l+1)
        return answer
                
