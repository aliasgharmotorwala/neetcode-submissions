class Solution:
    def isHappy(self, n: int) -> bool:

        # return False for negative integers
        if n < 0:
            return False

        unique_sums = set()

        def is_cyclic(num: int) -> bool:

            str_num = str(num)

            num_sum = 0

            for num in str_num:
                num_sum += (int(num))**2

            if num_sum == 1:
                return True
            
            if num_sum in unique_sums:
                return False
            
            unique_sums.add(num_sum)

            return is_cyclic(num_sum)


        return is_cyclic(n)




        