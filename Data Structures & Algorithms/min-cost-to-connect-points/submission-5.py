class minHeap:

    def __init__(self):

        self.heap = []

    def add(self, dist: Tuple(int, List[int])):

        self.heap.append(dist)

        i = len(self.heap)-1

        while i>0:

            parent = (i-1)//2

            if self.heap[i][0] < self.heap[parent][0]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_value = self.heap.pop()

        i = 0

        while i<len(self.heap):

            m = i

            left = 2*i + 1
            right = 2*i + 2

            if left < len(self.heap) and self.heap[m][0] > self.heap[left][0]:
                m = left
            if right < len(self.heap) and self.heap[m][0] > self.heap[right][0]:
                m = right
            if m != i:
                self.heap[m], self.heap[i] = self.heap[i], self.heap[m]
                i = m
            else:
                break

        return min_value

    def len(self):
        return len(self.heap)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        lowest_dist = minHeap()
        
        point_to_use = points[0]

        seen_points = set()

        unseen_points = set()
        for point in points:
            unseen_points.add((point[0], point[1]))

        min_cost = 0

        while len(seen_points) <= len(points):

            seen_points.add((point_to_use[0], point_to_use[1]))

            points_to_iter = unseen_points - seen_points

            for point in points_to_iter:

                dist = abs(point_to_use[0]-point[0]) + abs(point_to_use[1]-point[1])

                lowest_dist.add((dist, point))

            if len(seen_points) == len(points):
                break
            
            while lowest_dist.len() > 0:
                min_dist, point_to_use = lowest_dist.pop()
                if point_to_use not in seen_points:
                    break

            if not min_dist:
                break
                
            min_cost += min_dist
                

                #min_heap.add((dist, point))


            #while min_heap.len() > 0:
            #    dist, next_point = min_heap.pop()
            #    if next_point in points:
            #        min_cost += dist
            #        point_to_use = next_point
            #        break

        return min_cost

        