class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points
        answer = []
        distance = []
        for point in points:
            pair = []
            dis = (point[0] ** 2) + (point[1] ** 2)
            pair.append(tuple(point))
            pair.append(dis)
            distance.append(pair)
        final = sorted(distance, key=lambda x: x[1])
        for i in range(k):
            answer.append(final[i][0])
        return answer
        
