class Solution:
    def rob(self, nums: List[int]) -> int:

        mem = {}

        def rob_next(house_num, startWithZero):

            if (house_num, startWithZero) in mem:
                return mem[(house_num, startWithZero)]

            if house_num >= len(nums):
                return 0

            if startWithZero and house_num == len(nums)-1:
                return 0

            next_best_step = max(rob_next(house_num+2, startWithZero), rob_next(house_num+3, startWithZero))

            mem[(house_num, startWithZero)] = nums[house_num] + next_best_step

            return mem[(house_num, startWithZero)]

        return max(nums[0]+rob_next(2, True), rob_next(1, False), nums[0]+rob_next(3, True), rob_next(2, False))
        