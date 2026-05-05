class Solution:
    def search(self, nums: List[int], target: int) -> int:

        middle_index = int(len(nums)/2)
        focus_list = nums
        index_start = 0

        while len(focus_list) > 0:
            if target == focus_list[middle_index]:
                if middle_index != 0:
                    return index_start + middle_index
                elif index_start != 0:
                    return index_start + 1
                else:
                    return middle_index
            elif len(focus_list) == 1:
                return -1
            elif target < focus_list[middle_index]:
                focus_list = focus_list[:middle_index]
            else:
                focus_list = focus_list[middle_index:]
                index_start += middle_index
            middle_index = int(len(focus_list)/2)
        
        return -1


        