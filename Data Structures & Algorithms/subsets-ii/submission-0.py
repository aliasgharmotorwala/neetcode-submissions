class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        subsets = []

        def backtrack(index, subset):

            if index == len(nums):
                return subsets.append(subset[:])

            
            subset.append(nums[index])
            backtrack(index+1, subset) # (1, [7]), (2, [7,7])
            subset.pop()

            while index + 1 <= len(nums)-1 and nums[index] == nums[index+1]:
                index += 1
            backtrack(index+1, subset)

        nums.sort() # [7,7]

        backtrack(0, [])

        return subsets
        