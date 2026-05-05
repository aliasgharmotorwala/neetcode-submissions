class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for first in range(len(numbers)):
            for second in range(first+1, len(numbers)):
                if numbers[first]+numbers[second] == target:
                    return [first+1, second+1]
        
        return []
        