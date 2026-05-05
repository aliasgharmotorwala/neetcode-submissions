class Solution:
    def rob(self, nums: List[int]) -> int:

        mem = {}
        
        def rob_next(house_num):

            if house_num in mem:
                return mem[house_num]

            if house_num >= len(nums):
                return 0
            
            mem[house_num] = max(nums[house_num] + rob_next(house_num+2), nums[house_num] + rob_next(house_num+3))
            return mem[house_num]

        return max(nums[0]+rob_next(2), rob_next(1), nums[0]+rob_next(3))
        