class Solution:
    def sortSentence(self, s: str) -> str:
        str_list = list(s.split())
        str_list.sort(key=lambda x: int(x[-1]))
        ans = ""
        for s in str_list:
            ans += s[:len(s)-1]
            ans += " "
        return ans.strip()

        
