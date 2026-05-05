class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_count = dict()
        char2_count = dict()
        for char in s:
            if char not in character_count:
                character_count.update({char:1})
            else:
                character_count[char] += 1
        for char2 in t:
            # If the character is not present in 1st string
            if char2 not in character_count:
                return False
            else:
                if not char2_count.get(char2):
                    char2_count.update({char2:1})
                else:
                    char2_count[char2] += 1
                # If occurence of a character is greater than 1st string
                if char2_count[char2] > character_count[char2]:
                    return False
        # Match all chars are same
        if len(character_count.keys()) != len(char2_count.keys()):
            return False
        # Match all chars occurence is same
        for char in character_count:
            if character_count[char] != char2_count[char]:
                return False

        return True

        