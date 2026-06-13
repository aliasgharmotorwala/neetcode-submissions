class MinHeap:
    def __init__(self, k):
        self.min_heap = []
        self.heap_length = k

    def add(self, val) -> None:

        self.min_heap.append(val)

        i = len(self.min_heap)-1

        while i>0:

            parent = (i-1)//2

            if self.min_heap[i] <= self.min_heap[parent]:
                self.min_heap[i], self.min_heap[parent] = self.min_heap[parent], self.min_heap[i]
                i = parent
            else:
                break
    
        if len(self.min_heap) > self.heap_length:
            self.popMin()

    def popMin(self) -> int:
        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]
        min_value = self.min_heap.pop()

        i = 0

        while i<len(self.min_heap):

            m = i
            left = 2*i + 1
            right = 2*i + 2

            if left < len(self.min_heap) and self.min_heap[left] < self.min_heap[m]:
                m = left
            if right < len(self.min_heap) and self.min_heap[right] < self.min_heap[m]:
                m = right
            if i != m:
                self.min_heap[i], self.min_heap[m] = self.min_heap[m], self.min_heap[i]
                i = m
            else:
                break

        return min_value

    def popkthvalue(self):
        return self.min_heap[0]



class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        self.min_heap = MinHeap(k)

        for num in nums:
            self.min_heap.add(num)

        return self.min_heap.popkthvalue()
        