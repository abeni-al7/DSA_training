class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True
        l, r = 0, 0
        while l < len(name) and r < len(typed):
            if name[l] == typed[r]:
                l += 1
                r += 1
            elif l != 0 and typed[r] == name[l-1]:
                while r < len(typed) and typed[r] == name[l-1]:
                    r += 1
            else:
                return False
        if l < len(name):
            return False
        while r < len(typed) and typed[r] == name[len(name) - 1]:
            r += 1
        if r < len(typed):
            return False
        return True
        
