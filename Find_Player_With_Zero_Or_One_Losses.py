class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = []
        mydict = defaultdict(list)
        for i in range(len(matches)):
            if mydict.get(matches[i][0], 0) > 0:
                pass
            else:
                mydict[matches[i][0]] = 0
            if mydict.get(matches[i][1], 0) > 0:
                mydict[matches[i][1]] += 1
            else:
                mydict[matches[i][1]] = 1
        lost0 = []
        lost1 = []
        for key, value in mydict.items():
            if value == 0:
                lost0.append(key)
            if value == 1:
                lost1.append(key)
        lost0.sort()
        lost1.sort()
        answer.append(lost0)
        answer.append(lost1)
        return answer
