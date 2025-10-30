class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = str(n)
        product = 1
        total = 0

        for digit in num:
            product *= int(digit)
            total += int(digit)

        return product - total
