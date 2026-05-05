class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        last_digit = len(digits) - 1

        add_one = False

        while last_digit >= 0:

            # for digits < 9, just add one to them and then return
            if digits[last_digit] <9:
                new_value = digits[last_digit] + 1
                digits[last_digit] = new_value
                break

            # if this is the first digit, then set the add_one flag to add one before it
            elif last_digit == 0:
                add_one = True
                
                
            # if digit is 9, then make it zero and add one to left side digit
            digits[last_digit] = 0
            last_digit -= 1

        if add_one:
            digits.insert(0, 1)

        return digits


