class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def dfs(row, col):

            if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0 or board[row][col] != 'O':
                return

            board[row][col] = 'E'

            for position in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                row_new = row+position[0]
                col_new = col+position[1]

                dfs(row_new, col_new)

            return

        for row in range(len(board)):
            dfs(row, 0)
            dfs(row, len(board[0])-1)

        for col in range(len(board[0])):
            dfs(0, col)
            dfs(len(board)-1, col) 

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'E':
                    board[row][col] = 'O'

        
                

            


            

            

