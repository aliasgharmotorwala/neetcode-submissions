class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        subsets = []
        
        def backtrack(num, pattern):

            if num >= n:
                return subsets.append(pattern)

            i = -1
            while pattern[i] == ")":
                i -= 1
                new_pattern = f"{pattern[:len(pattern)+i+1]}(){pattern[len(pattern)+i+1:]}"
                backtrack(num+1, new_pattern)


            backtrack(num+1, f"{pattern}()")


        backtrack(1, "()")

        return subsets
        

            
        