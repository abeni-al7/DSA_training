class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer = []
        l, r = 0, 0
        while l < len(firstList) and r < len(secondList):
            if firstList[l][0] <= secondList[r][1] and secondList[r][0] <= firstList[l][1]:
                temp = []
                temp.append(max(firstList[l][0], secondList[r][0]))
                temp.append(min(firstList[l][1], secondList[r][1]))
                answer.append(temp)
            if firstList[l][1] >= secondList[r][1]:
                r += 1
            else:
                l += 1
        return answer
