# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[-1])
        transpose = [[0] * rows for _ in range(cols)]
        print(transpose)
        for i in range(rows):
            for j in range(cols):
                transpose[j][i] = matrix[i][j]
        
        return transpose