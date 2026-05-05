class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if len(grid) < 1:
            return None

        allowed_pos = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right

        r_max = len(grid)
        c_max = len(grid[0])

        def bfs(i, j, cost_to_chest):

            for pos in allowed_pos:

                r = i + pos[0]
                c = j + pos[1]

                # if hit outside boundary
                if r<0 or c<0 or r>=r_max or c>=c_max:
                    continue

                if grid[r][c] not in [-1, 0]: #traversing point not water or chest
                    new_cost = cost_to_chest + 1
                    if grid[r][c] > new_cost:
                        grid[r][c] = new_cost
                        bfs(r, c, new_cost)


        for i in range(0, r_max):
            for j in range(0, c_max):

                # Found the chest
                if grid[i][j] == 0:
                    bfs(i, j, 0)
        