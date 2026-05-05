class Solution:
    def canJump(self, nums: List[int]) -> bool:

        mem = {}

        def dp(index, jump):

            if (index, jump) in mem:
                return mem[(index, jump)]

            dst = index + jump

            result = False

            if dst == len(nums) - 1:
                result = True
            elif dst > len(nums) - 1:
                result = False
            elif nums[dst] == 0:
                result = False
            else:
                for new_jump in range(nums[dst],0,-1):
                    if dp(dst, new_jump):
                        result = True
                        break

            mem.update({(index, jump): result})
            
            return result

        return dp(0, 0)

'''
        if len(nums) == 1:
            return True

        i = 0

        while i < len(nums):

            if nums[i] == 0 and i != len(nums)-1:
                break
            
            i = i + nums[i]

            if i == len(nums) - 1:
                return True
        
        return False
'''
        