class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 1:
            return 0

        max_length = 1

        l = 0
        while l < len(s):
            r = l+1
            sub_string = s[l]
            while r < len(s):
                if s[r] not in sub_string:
                    sub_string += s[r]
                    if len(sub_string) > max_length:
                        max_length = len(sub_string)
                    r += 1
                else:
                    break
            l += 1
                    

        
        return max_length