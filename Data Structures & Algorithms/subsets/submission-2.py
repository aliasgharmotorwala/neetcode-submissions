class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = list()

        def backtrack(index, path):

            # Base case
            if index == len(nums):
                return subsets.append(path[:])

            # make choice
            path.append(nums[index])
            backtrack(index+1, path)

            # backtrack, and select other path
            path.pop()

            backtrack(index+1, path)

        backtrack(0, [])
        
        return subsets
        
        