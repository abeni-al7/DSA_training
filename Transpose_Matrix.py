class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        index = 0

        while index < len(matrix[0]):
            nums = []
            for i in range(len(matrix)):
                nums.append(matrix[i][index])
            index += 1
            transpose.append(nums)
        return transpose
