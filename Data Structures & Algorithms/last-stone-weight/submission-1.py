class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        self._stones = list()

        # First sort the list
        for stone in stones:
            self.add(stone)
        
        # Remove elements until there is one or no element remaining
        while len(self._stones) > 1:
            highest = self.popMax()
            second_highest = self.popMax()

            difference = highest - second_highest

            if difference > 0:
                self.add(difference)

        return self._stones[0] if len(self._stones) == 1 else 0
        
    def add(self, stone): # [6, 4, 3, 2, 2], [3,2,2,2], [2,2,1]

        self._stones.append(stone)

        i = len(self._stones) - 1

        while i>0:
            parent = (i-1)//2

            if self._stones[i] >= self._stones[parent]:
                self._stones[i], self._stones[parent] = self._stones[parent], self._stones[i]
                i = parent
            else:
                break

    def popMax(self): # (6, [4,2,3,2]), (4, [3,2,2]), (3, [2,2,2]), (2, [2,2]), (2, [2,1]), (2, [1]))
        self._stones[0], self._stones[-1] = self._stones[-1], self._stones[0]
        max_value = self._stones.pop()

        n = len(self._stones)

        highest = 0
        i = 0

        while True:
            left = 2*i+1
            right = 2*i+2
            if left < n and self._stones[left] > self._stones[highest]:
                highest = left
            if right < n and self._stones[right] > self._stones[highest]:
                highest = right

            if highest != i:
                self._stones[highest], self._stones[i] = self._stones[i], self._stones[highest]
                i = highest
            else:
                break
            
        return max_value

        

        
