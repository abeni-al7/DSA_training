class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_matrix = []
        for r in image:
            new_r = r[::-1]
            new_matrix.append(new_r)
        for r in range(len(image)):
            for c in range(len(image[r])):
                if new_matrix[r][c] == 0:
                    new_matrix[r][c] = 1
                else:
                    new_matrix[r][c] = 0
        return new_matrix
        
