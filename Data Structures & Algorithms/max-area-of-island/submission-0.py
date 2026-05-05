class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_count = 0

        islands_list = []

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):

                if grid[i][j] == 1:

                    if len(islands_list) == 0:
                        new_island = {(i, j)}
                        islands_list.append(new_island)
                        max_count = 1
                        continue

                    islands_to_be_added = list()
                    for island in islands_list:
                        if (i+1<len(grid) and (i+1, j) in island) or \
                        (i-1>=0 and (i-1, j) in island) or \
                        (j+1<len(grid[i]) and (i, j+1) in island) or \
                        (j-1>=0 and (i, j-1) in island):
                            islands_to_be_added.append(island)

                    new_island = set()
                    for island in islands_to_be_added:
                        new_island.update(island)
                        islands_list.remove(island)
                    new_island.add((i, j))
                    islands_list.append(new_island)
                    new_island_area = len(new_island)
                    if new_island_area > max_count:
                        max_count = new_island_area
                    
        return max_count