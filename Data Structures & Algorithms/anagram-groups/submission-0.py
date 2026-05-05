class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_dict = {}

        for word in strs:

            list_str = list(word)

            list_str.sort()

            sorted_str = "".join(list_str)

            if sorted_str not in anagrams_dict:
                anagrams_dict.update({sorted_str: [word]})
            else:
                anagrams_dict[sorted_str].append(word)
            
        final_list = []

        for key, value in anagrams_dict.items():
            final_list.append(value)

        return final_list
        