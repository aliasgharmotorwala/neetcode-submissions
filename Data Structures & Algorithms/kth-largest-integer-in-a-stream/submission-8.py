class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self._kth_index = k
        self._descending_order_list = []

        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:

        existing_nums_len = len(self._descending_order_list)

        # if no num in list
        if existing_nums_len == 0:
            self._descending_order_list.append(val)

        existing_nums_index = 0

        while existing_nums_index < existing_nums_len:

            if val >= self._descending_order_list[existing_nums_index]:
                self._descending_order_list.insert(existing_nums_index, val)
                break

            elif existing_nums_len == 1 or existing_nums_index == (existing_nums_len-1):
                self._descending_order_list.append(val)
                break

            elif val > self._descending_order_list[existing_nums_index+1]:
                self._descending_order_list.insert(existing_nums_index+1, val)
                break
        
            existing_nums_index += 1

        if self._kth_index > len(self._descending_order_list):
            return None

        return self._descending_order_list[self._kth_index - 1]