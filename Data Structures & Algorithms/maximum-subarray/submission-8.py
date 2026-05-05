class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        self.max_sum = nums[0]

        sum = 0
        for num in nums:
            sum += num
            if num > sum:
                sum = num
            self.max_sum = max(self.max_sum, sum)
        return self.max_sum


'''
        def get_sum(index, sum):

            if index >= len(nums):
                return

            if nums[index] > self.max_sum:
                self.max_sum = nums[index]

            # add num to existing sum
            new_sum = sum + nums[index]
            if new_sum > self.max_sum:
                self.max_sum = new_sum

            if nums[index] > new_sum:
                get_sum(index+1, nums[index])
            else:
                get_sum(index+1, new_sum)

        get_sum(0, 0)
'''

# [2] -> 2
# [2,-3] = -1
# [2,-3, 4] = 3
# [2,-3, 4, -2] = 1
# [2,-3, 4, -2, 2] = 3
# [2,-3, 4, -2, 2, 1] = 4
# [2,-3, 4, -2, 2, 1, -1] = 3
# [2,-3, 4, -2, 2, 1, -1, 4] = 7
# [-3] = -3 
# [-3, 4] = 1
# [-3, 4, -2] = -3
# [-3, 4, -2, 2] = -1
# [-3, 4, -2, 2, 1] = 0
# [-3, 4, -2, 2, 1, -1] = -1
# [-3, 4, -2, 2, 1, -1, 4] = 3
# [4] = 4
# [4, -2] = 2
# [4, -2, 2] = 4
# [4, -2, 2, 1] = 5
# [4, -2, 2, 1, -1] = 4
# [4, -2, 2, 1, -1, 4] = 8
# [-2] = -2
# [-2, 2] = 0
# [-2, 2, 1] = 1
# [-2, 2, 1, -1] = 0
# [2] = 2
# [2, 1] = 3
# [2, 1, -1] = 2
# [1] = 1
# [1, -1] = 0
# [-1] = -1

  


        