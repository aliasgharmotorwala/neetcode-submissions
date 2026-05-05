class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands_list = []

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):

                # if the point is land
                if grid[i][j] == "1":

                    # if there are no existing islands
                    if len(islands_list) == 0:
                        new_island = {(i, j)}
                        islands_list.append(new_island)
                        continue

                    # check with existing islands
                    islands_to_be_added = list()
                
                    for island in islands_list:

                        #check left point
                        if j-1 >= 0 and (i, j-1) in island:
                            islands_to_be_added.append(island)
                        
                        #check top point
                        elif i-1 >= 0 and (i-1, j) in island:
                            islands_to_be_added.append(island)

                        #check bottom point
                        elif i+1 < len(grid) and (i+1, j) in island:
                            islands_to_be_added.append(island)

                        #check right point
                        elif j+1 < len(grid[i]) and (i, j+1) in island:
                            islands_to_be_added.append(island)

                    # combine all the islands connecting this point
                    new_island = set()
                    for island in islands_to_be_added:
                        new_island.update(island)
                        islands_list.remove(island)

                    # add this point to the new island
                    new_island.add((i, j))

                    # add the new island to the island list
                    islands_list.append(new_island)

        return len(islands_list)

                    