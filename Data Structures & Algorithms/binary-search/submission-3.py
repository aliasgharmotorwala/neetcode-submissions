class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            middle_index = (left_pointer+right_pointer)//2
            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] > target:
                right_pointer = middle_index - 1
            else:
                left_pointer = middle_index + 1
        
        return -1


        