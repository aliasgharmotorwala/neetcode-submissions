import re

def is_alphanumeric(s: str) -> bool:
    if re.match('[a-zA-Z0-9]', s):
        return True
    return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while end > start:
            if not is_alphanumeric(s[start]):
                start += 1
            elif not is_alphanumeric(s[end]):
                end -= 1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1
        
        return True
        