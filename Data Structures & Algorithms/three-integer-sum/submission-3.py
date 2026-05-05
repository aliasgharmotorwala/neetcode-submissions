class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def merge_sort(nums):

            if len(nums) == 1:
                return nums

            m = len(nums) // 2

            left = nums[:m]
            right = nums[m:]

            merge_sort(left)
            merge_sort(right)

            l = r = i = 0

            while l<len(left) and r<len(right):
                if left[l] < right[r]:
                    nums[i] = left[l]
                    l += 1
                else:
                    nums[i] = right[r]
                    r += 1
                i += 1  

            while l < len(left):
                nums[i] = left[l]
                l += 1
                i += 1
            while r < len(right):
                nums[i] = right[r]
                r += 1
                i += 1

        output = []

        merge_sort(nums)

        distinct_nums = set()

        for i in range(len(nums)):
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            while j<k:
                sum = nums[j]+nums[k]
                if sum == target:
                    if [nums[i], nums[j], nums[k]] not in output:
                        output.append([nums[i], nums[j], nums[k]])
                    j += 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1

        return output



        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        if temp not in output:
                            output.append(temp)
        
        return output




            