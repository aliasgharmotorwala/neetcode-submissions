class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combinations = []

        def backtrack(index, comb, sum):

            # base case
            if index >= len(nums) or sum >= target:
                if sum == target:
                    combinations.append(comb[:])
                return
            
            # Include the index num
            sum += nums[index]
            comb.append(nums[index])
            if sum <= target:
                backtrack(index, comb, sum) # (1, [2,2,5], 9), 
            sum -= nums[index]
            comb.pop()

            # Dont include the index num
            backtrack(index+1, comb, sum) # (1, [2,2], 4), 

        backtrack(0, [], 0)

        return combinations
        