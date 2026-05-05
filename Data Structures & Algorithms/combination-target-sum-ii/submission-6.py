class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        combinations = []

        def backtrack(index, comb, sum):

            # base case
            if index >= len(candidates) or sum >= target:
                if sum == target:
                    combinations.append(comb[:])
                return

            # use index num
            sum += candidates[index]
            comb.append(candidates[index])
            if sum <= target:
                backtrack(index+1, comb, sum) # (0, [9], 9)=> None, (2, [2], 2), (3, [2, 2], 4), (4, [2, 2, 4], 8)
            sum -= candidates[index]
            comb.pop()

            # without index num
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            backtrack(index+1, comb, sum) # (1, [], 0)

        candidates.sort()
        backtrack(0, [], 0)

        return combinations
        