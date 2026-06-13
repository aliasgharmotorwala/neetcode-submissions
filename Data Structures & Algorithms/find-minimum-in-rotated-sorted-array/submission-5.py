class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)
        max_num = None

        if len(nums) == 1:
            return nums[0]

        while l <= r:

            m = (l+r)//2

            # if the next number is smaller than its the smallest
            if m+1 < len(nums) and nums[m+1] < nums[m]:
                return nums[m+1]
            elif m+1 >= len(nums) and nums[0] < nums[m]:
                return nums[0]

            # if previous number is bigger than the current is smallest
            elif (m-1 >= 0 and nums[m-1] > nums[m]) or (m-1<0 and nums[-1] > nums[m]):
                return nums[m]
            
            # consider next numbers, if series is ascending
            if not max_num:
                max_num = m
                l = m + 1
            elif nums[m] > nums[max_num]:
                max_num = m
                l = m + 1
            # consider stoping going ahead if the numbers are decreasing
            else:
                r = m - 1
                
            if l >= len(nums):
                l = 0


            
        