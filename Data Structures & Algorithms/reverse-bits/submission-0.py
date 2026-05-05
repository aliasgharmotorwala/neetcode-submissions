class Solution:
    def reverseBits(self, n: int) -> int:

        answer = 0

        bit_value = 1

        for i in range(32):

            if n & bit_value:
                answer += 2**(31-i)

            bit_value = bit_value << 1

        return answer
            
