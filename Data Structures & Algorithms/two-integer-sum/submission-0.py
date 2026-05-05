class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_accessed_nums = []
        for index1, num in enumerate(nums):
            for index2, other_num in enumerate(already_accessed_nums):
                if (num+other_num) == target:
                    return [index2, index1]
            already_accessed_nums.append(num)
        return []
        