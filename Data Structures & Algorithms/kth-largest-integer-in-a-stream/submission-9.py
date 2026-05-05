class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self._kth_index = k
        self._min_heap = []

        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:

        self._min_heap.append(val)

        i = len(self._min_heap)-1
        while i>0:
            parent = (i-1)//2
            if self._min_heap[i] <= self._min_heap[parent]:
                self._min_heap[i], self._min_heap[parent] = self._min_heap[parent], self._min_heap[i]
                i = parent
            else:
                break
            
        if len(self._min_heap) > self._kth_index:
            self._min_heap[0], self._min_heap[-1] = self._min_heap[-1], self._min_heap[0]
            self._min_heap.pop()

            n = len(self._min_heap)
            smallest = 0
            i = 0
            while True:
                left = 2*i+1
                right = 2*i+2

                if left < n and self._min_heap[smallest] > self._min_heap[left]:
                    smallest = left
                if right < n and self._min_heap[smallest] > self._min_heap[right]:
                    smallest = right
                if smallest != i:
                    self._min_heap[i], self._min_heap[smallest] = self._min_heap[smallest], self._min_heap[i]
                    i = smallest
                else:
                    break

        return self._min_heap[0]

