class Solution:
    def hammingWeight(self, n: int) -> int:

        testing_integer = 1

        count_ones = 0

        for i in range(0, 32):

            shifted_integer = testing_integer << i

            if shifted_integer & n == shifted_integer:
                count_ones += 1

        return count_ones
        