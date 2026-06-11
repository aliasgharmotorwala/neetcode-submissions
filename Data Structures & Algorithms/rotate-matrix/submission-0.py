class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        temp_rows = []

        col = 0
        
        while col < len(matrix):
            temp = []
            for row in range(len(matrix)-1, -1, -1):
                temp.append(matrix[row][col])
            temp_rows.append(temp)
            col += 1

        for row in range(0, len(matrix)):
            matrix[row] = temp_rows[row]        