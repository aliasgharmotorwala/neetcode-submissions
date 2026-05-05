class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()
        for num in nums:
            if num not in unique_values:
                unique_values.add(num)
            else:
                return True
        return False
        