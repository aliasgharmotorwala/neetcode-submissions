class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        self.max_heap = []
        self.max_heap_dist = []

        def add(point):

            dist_to_o = math.sqrt((abs(point[0]) - 0)**2 + (abs(point[1]) - 0)**2)

            self.max_heap_dist.append(dist_to_o)
            self.max_heap.append(point)

            i = len(self.max_heap_dist) - 1

            while i > 0:

                parent = (i-1)//2

                if self.max_heap_dist[i] >= self.max_heap_dist[parent]:
                    self.max_heap_dist[i], self.max_heap_dist[parent] = self.max_heap_dist[parent], self.max_heap_dist[i]
                    self.max_heap[i], self.max_heap[parent] = self.max_heap[parent], self.max_heap[i]
                    i = parent
                else:
                    break

            if len(self.max_heap_dist) > k:
                self.max_heap_dist[0], self.max_heap_dist[-1] = self.max_heap_dist[-1], self.max_heap_dist[0]
                self.max_heap[0], self.max_heap[-1] = self.max_heap[-1], self.max_heap[0]
                self.max_heap_dist.pop()
                self.max_heap.pop()

                i = 0

                while i < len(self.max_heap_dist):

                    m = i

                    left = (2*i)+1
                    right = (2*i)+2

                    if left < len(self.max_heap_dist) and self.max_heap_dist[m] < self.max_heap_dist[left]:
                        m = left
                    if right < len(self.max_heap_dist) and self.max_heap_dist[m] < self.max_heap_dist[right]:
                        m = right
                    if m != i:
                        self.max_heap_dist[i], self.max_heap_dist[m] = self.max_heap_dist[m], self.max_heap_dist[i]
                        self.max_heap[i], self.max_heap[m] = self.max_heap[m], self.max_heap[i]
                        i = m
                    else:
                        break

        for point in points:
            add(point)

        return self.max_heap

        