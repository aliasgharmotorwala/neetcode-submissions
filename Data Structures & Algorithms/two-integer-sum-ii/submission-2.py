class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for first in range(len(numbers)):

            l = first + 1
            r = len(numbers) - 1
            complement = target - numbers[first]
            while l <= r:
                mid = (l+r)//2
                if numbers[mid] == complement:
                    return [first+1, mid+1]
                elif numbers[mid] < complement:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
        