class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ["[", "{", "("]
        close_brackets = ["]", "}", ")"]
        s_brackets = []


        for char in s:
            if char in open_brackets:
                s_brackets.append(char)
            elif char in close_brackets:
                try:
                    last_open = s_brackets.pop()
                except:
                    return False
                bracket_type = close_brackets.index(char)
                if last_open != open_brackets[bracket_type]:
                    return False

        if len(s_brackets) != 0:
            return False

        return True
        