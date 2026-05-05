class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left_row = 0
        right_row = len(matrix) - 1

        while left_row <= right_row:

            middle_row = (left_row+right_row)//2

            row_min = matrix[middle_row][0]
            row_max = matrix[middle_row][-1]

            if target == row_min or target == row_max:
                return True

            elif target < row_min:
                right_row = middle_row - 1

            elif target > row_min and target < row_max:

                row_left = 0
                row_right = len(matrix[middle_row])

                while row_left <= row_right:
                    row_mid = (row_left+row_right)//2
                    row_mid_value = matrix[middle_row][row_mid]
                    if target == row_mid_value:
                        return True
                    elif target > row_mid_value:
                        row_left = row_mid+1
                    else:
                        row_right = row_mid-1
                
                return False

            elif target > row_max:
                left_row = middle_row + 1

        return False