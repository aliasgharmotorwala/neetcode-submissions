class Solution:
    def countBits(self, n: int) -> List[int]:

        output = list()

        for i in range(n+1):
            output.append(count_ones(i))

        return output

def count_ones(num: int) -> int:

    check_int = 1

    counts = 0

    while check_int <= num:

        if check_int & num:
            counts += 1
            
        check_int = check_int << 1

    return counts

    # 000
    # 001
    # 010
    # 011
    # 100
            

        