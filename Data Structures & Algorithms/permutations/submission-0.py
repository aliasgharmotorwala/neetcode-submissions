class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        permutations = []

        def backtrack(cur_list, free_nums):

            # base case
            if len(cur_list) == len(nums):
                return permutations.append(cur_list[:])

            # Use index
            for i in free_nums:
                free_nums2 = free_nums[:]
                cur_list.append(i)
                free_nums2.remove(i)
                backtrack(cur_list, free_nums2[:]) # ([1,2,3], [])
                cur_list.pop()


        backtrack([], nums[:])

        return permutations

# ([1], [2,3]), ([1,2], [3]),