from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if len(grid) < 1:
            return None

        allowed_pos = [(-1, 0), (1, 0), (0, -1), (0,1)]

        r_max = len(grid)
        c_max = len(grid[0])

        queue = deque()
        visited_nodes = set()
        visited_oranges = set()
        oranges = set()

        # Get all the rotten fruits first
        for r in range(0, r_max):
            for c in range(0, c_max):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited_nodes.add((r, c))

                if grid[r][c] in [1, 2]:
                    oranges.add((r, c))


        def addCell(r, c):

            if (r, c) in visited_nodes:
                return

            if r<0 or c<0 or r>=r_max or c>=c_max:
                return

            if grid[r][c] == 1:
                queue.append((r, c))
            
            visited_nodes.add((r, c))

        max_dist = -1

        if len(oranges) == 0:
            return 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                visited_oranges.add((r, c))
                for pos in allowed_pos:
                    addCell(r+pos[0], c+pos[1])
            max_dist += 1

        # if there is a node not connecting to any orange
        if len(oranges) != len(visited_oranges):
            return -1

        return max_dist

        