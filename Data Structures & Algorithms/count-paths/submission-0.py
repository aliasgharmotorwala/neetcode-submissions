class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        mem = {}

        count = 0

        def paths(i , j):

            if (i, j) in mem:
                return mem[(i, j)]

            # reached limit
            if i > m-1 or j > n-1:
                return 0
            
            elif i == m-1 and j == n-1:
                return 1

            else:
                down = paths(i+1, j)
                right = paths(i, j+1)

            total_paths = down+right

            mem.update({(i, j): total_paths})
            
            return total_paths

        return paths(0,0)
        