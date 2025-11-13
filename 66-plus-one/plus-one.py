class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for digit in digits:
            digit = str(digit)
            num += digit

        number = int(num)
        number += 1
        num = str(number)
        digits = list(num)
        for i in range(len(digits)):
            digits[i] = int(digits[i])
        return digits
