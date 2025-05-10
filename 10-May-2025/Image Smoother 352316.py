# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[-1])
        smooth = [[0 for _ in range(cols)] for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        inbound = lambda r, c: 0 <= r < rows and 0 <= c < cols

        for i in range(rows):
            for j in range(cols):
                total = img[i][j]
                count = 1
                for direction in directions:
                    r, c = i + direction[0], j + direction[1]
                    if inbound(r, c):
                        total += img[r][c]
                        count += 1
                smooth[i][j] = floor(total / count)
        return smooth