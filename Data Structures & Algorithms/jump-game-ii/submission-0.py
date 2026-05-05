class Solution:
    def jump(self, nums: List[int]) -> int:

        goal = len(nums) - 1

        jumps = 0

        start = 0

        while start < goal:

            for jump in range(nums[start],0,-1):
                if start + jump == goal:
                    goal = start
                    start = -1
                    jumps += 1
                    break
            
            start += 1

        return jumps
        