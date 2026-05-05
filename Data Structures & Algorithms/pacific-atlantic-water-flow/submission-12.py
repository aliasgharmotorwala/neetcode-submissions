from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        result = []
        
        if len(heights) < 1:
            return []
        
        allowed_pos = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        r_max = len(heights)
        c_max = len(heights[0])

        visited_nodes_p = {}
        visited_nodes_a = {}

        def dfs(r, c, visited_nodes):

            for pos in allowed_pos:

                neighbor = (r+pos[0], c+pos[1])

                if (neighbor[0], neighbor[1]) in visited_nodes:
                    continue

                if neighbor[0] < 0 or neighbor[0] >= r_max:
                    continue

                if neighbor[1] < 0 or neighbor[1] >= c_max:
                    continue

                if heights[neighbor[0]][neighbor[1]] >= heights[r][c]:
                    visited_nodes.add((neighbor[0], neighbor[1]))
                    dfs(neighbor[0], neighbor[1], visited_nodes)

        pacific_nodes = set() # {(0,0), (1,0), (0,1), (1,1), (0,2), (1,2), (0,3), (1,3), (0,4)-,}
        for col in range(c_max):
            pacific_nodes.add((0, col))
            dfs(0, col, pacific_nodes)
        for row in range(1,r_max):
            pacific_nodes.add((row, 0))
            dfs(row, 0, pacific_nodes)

        atlantic_nodes = set()
        for col in range(c_max):
            atlantic_nodes.add((r_max-1, col))
            dfs(r_max-1, col, atlantic_nodes)
        for row in range(0,r_max-1):
            atlantic_nodes.add((row, c_max-1))
            dfs(row, c_max-1, atlantic_nodes)

        result_nodes = pacific_nodes.intersection(atlantic_nodes)

        for node in result_nodes:
            result.append([node[0], node[1]])
        result.sort()

        return result 


'''
        def bfs_pacific(r, c):

            if (r, c) in visited_nodes_p:
                return visited_nodes_p[(r, c)]

            pacific = False

            if r<=0 or c<=0:
                pacific = True

            for pos in allowed_pos:

                if pacific == True:
                    break

                neighbor = (r+pos[0], c+pos[1])

                if neighbor[0] < 0 or neighbor[0] >= r_max:
                    continue

                if neighbor[1] < 0 or neighbor[1] >= c_max:
                    continue

                if heights[neighbor[0]][neighbor[1]] <= heights[r][c]:
                    if bfs_pacific(neighbor[0], neighbor[1]):
                        pacific = True
                        break

            visited_nodes_p.update({(r, c): pacific})

            return pacific

        def bfs_atlantic(r, c):

            if (r, c) in visited_nodes_a:
                return visited_nodes_a[(r, c)]

            atlantic = False

            if r>=(r_max-1) or c>=(c_max-1):
                atlantic = True

            for pos in allowed_pos:

                if atlantic == True:
                    break

                neighbor = (r+pos[0], c+pos[1])

                if neighbor[0] < 0 or neighbor[0] >= r_max:
                    continue

                if neighbor[1] < 0 or neighbor[1] >= c_max:
                    continue

                if heights[neighbor[0]][neighbor[1]] <= heights[r][c]:
                    if bfs_atlantic(neighbor[0], neighbor[1]):
                        atlantic = True
                        break

            visited_nodes_a.update({(r, c): atlantic})

            return atlantic


        pacific_result = {}
        for r in range(r_max):
            for c in range(c_max):
                pacific_result.update({(r, c): bfs_pacific(r, c)})
        
        atlantic_result = {}
        for r in range(r_max-1,-1,-1):
            for c in range(c_max-1,-1,-1):
                atlantic_result.update({(r, c): bfs_atlantic(r, c)})
                if pacific_result[(r, c)] and atlantic_result[(r, c)]:
                    result.append([r, c])
'''
