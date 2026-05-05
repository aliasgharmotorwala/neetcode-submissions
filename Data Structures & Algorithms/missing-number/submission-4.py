class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sorted_nums = sorted(nums)
        
        if sorted_nums[0] != 0:
            return 0

        sequence_num = sorted_nums[0]

        for i in range(1, len(sorted_nums)):

            sequence_num += 1

            if sorted_nums[i] != sequence_num:
                return sequence_num

        return sequence_num + 1