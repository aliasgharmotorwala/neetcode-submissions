class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        original_len = len(matrix)

        col = 0
        
        while col < original_len:
            temp = []
            for row in range(original_len-1, -1, -1):
                temp.append(matrix[row][0])
                matrix[row].pop(0)
            matrix.append(temp)
            col += 1

        del matrix[:original_len]