class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        max_length = 0

        for i in range(len(s)):
            substring = s[i]
            length = 1
            replace = 0
            for nchar in range(i+1, len(s)):
                if s[nchar] == substring:
                    length += 1
                elif replace < k:
                    replace += 1
                    length += 1
                else:
                    break
            # add replacements before if possible
            b = i-1
            while b>=0 and replace < k:
                length += 1
                b -= 1
                replace += 1
            max_length = max(max_length, length)

        if max_length == len(s):
            return max_length

        for i in range(len(s)-1,-1,-1):
            substring = s[i]
            length = 1
            replace = 0
            for nchar in range(i-1, -1, -1):
                if s[nchar] == substring:
                    length += 1
                elif replace < k:
                    replace += 1
                    length += 1
                else:
                    break
            max_length = max(max_length, length)
        

        return max_length
        