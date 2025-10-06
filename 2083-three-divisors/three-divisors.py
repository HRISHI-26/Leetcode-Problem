class Solution:
    def isThree(self, n: int) -> bool:
        set_of_divisors = {divisor for divisor in range(1, n + 1) if n % divisor == 0}
        if len(set_of_divisors) == 3:
            return True
        return False
