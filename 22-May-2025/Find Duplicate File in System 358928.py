# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = defaultdict(list)
        for path in paths:
            files = path.split()
            for i in range(1, len(files)):
                name, content = files[i].split("(")
                content_dict[content[:-1]].append(files[0] + "/" + name)
        
        output = []
        for v in content_dict.values():
            if len(v) > 1:
                output.append(v)
        
        return output