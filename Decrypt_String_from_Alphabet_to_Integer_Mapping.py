class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypted = ""
        i = 0
        while i < len(s):
            st = ""
            if i + 2 < len(s) and s[i + 2] == '#':
                st += s[i]
                st += s[i+1]
                i += 3
            else:
                st += s[i]
                i += 1
            decrypted += chr(int(st) + 96)
        return decrypted

                    
