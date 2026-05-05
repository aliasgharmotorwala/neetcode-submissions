class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        number_frequency = {}

        for num in nums:

            if num not in number_frequency:
                number_frequency.update({num: 1})

            else:
                number_frequency[num] += 1

        
        self.heap_sort = []

        def add_to_heap(num, key):

            self.heap_sort.append(num)
            self.result.append(key)

            i = len(self.heap_sort) - 1

            while i > 0:
                parent = (i-1)//2

                if self.heap_sort[i] < self.heap_sort[parent]:
                    self.heap_sort[parent], self.heap_sort[i] = self.heap_sort[i], self.heap_sort[parent]
                    self.result[parent], self.result[i] = self.result[i], self.result[parent]
                    i = parent
                else:
                    break

            if len(self.heap_sort) > k:
                self.heap_sort[-1], self.heap_sort[0] = self.heap_sort[0], self.heap_sort[-1]
                self.result[-1], self.result[0] = self.result[0], self.result[-1]
                self.heap_sort.pop()
                self.result.pop()

                i = 0

                while i < len(self.heap_sort):
                    m = i
                    left = 2*i + 1
                    right = 2*i + 2

                    if left < len(self.heap_sort) and self.heap_sort[m] > self.heap_sort[left]:
                        m = left
                    if right < len(self.heap_sort) and self.heap_sort[m] > self.heap_sort[right]:
                        m = right
                    if m != i:
                        self.heap_sort[i], self.heap_sort[m] = self.heap_sort[m], self.heap_sort[i]
                        self.result[i], self.result[m] = self.result[m], self.result[i]
                        i = m
                    else:
                        break

        self.result = []

        for key, value in number_frequency.items():

            add_to_heap(value, key)

        return self.result
                    

