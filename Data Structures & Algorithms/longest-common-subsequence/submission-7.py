class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        visited = {}
        
        if len(text1) <= len(text2):
            txt1 = text1
            txt2 = text2
        else:
            txt1 = text2
            txt2 = text1

        if txt1 in txt2:
            return len(txt1)

        def dp(index1, index2):

            if (index1, index2) in visited:
                return visited[(index1, index2)]

            i = index1
            j = index2
            max_string = ""
            while i < len(txt1) and j < len(txt2):
                if txt1[i] == txt2[j]:
                    new_string = txt1[i] + dp(i+1, j+1)
                    if len(new_string) > len(max_string):
                        max_string = new_string
                
                if j < len(txt2)-1:
                    j += 1
                elif j == len(txt2)-1:
                    i += 1
                    j=index2

            visited_nodes = max_string

            return max_string

        return len(dp(0, 0))

        # (3, 1, "u")
        # (6, 4, "ur")
        # (3, 3, "abc")
        # (4, 4, "abcd")

        
        