# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        
        first = self.rotate(mat)
        if first == target:
            return True
        
        second = self.rotate(first)
        if second == target:
            return True
        
        third = self.rotate(second)
        if third == target:
            return True
        
        fourth = self.rotate(third)
        if fourth == target:
            return True
        return False
    
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        # Step 1: find transpose
        for i in range(n):
            for j in range(n):
                rotated[j][i] = matrix[i][j]
        
        # Step 2: reverse every row
        for row in rotated:
            row.reverse()
        return rotated