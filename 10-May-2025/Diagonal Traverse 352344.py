# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        i, j = 0, 0
        answer = []
        inbound = lambda x, y: 0 <= x < rows and 0 <= y < cols
        up = True
        while i < rows and j < cols:
            answer.append(mat[i][j])
            if i == 0 and up:
                if j == cols - 1:
                    i += 1
                else:
                    j += 1
                up = False
            elif j == cols - 1 and up:
                i += 1
                up = False
            elif j == 0 and not up and i != rows - 1:
                i += 1
                up = True
            elif i == rows - 1 and not up:
                j += 1
                up = True
            elif inbound(i - 1, j + 1) and up:
                i -= 1
                j += 1
            elif inbound(i + 1, j - 1) and not up:
                i += 1
                j -= 1
            else:
                break
        return answer