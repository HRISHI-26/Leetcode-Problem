class Solution:
    def isThree(self, n: int) -> bool:
        rem = [n % i for i in range(1, n + 1)]
        if rem.count(0) == 3:
            return True
        return False
