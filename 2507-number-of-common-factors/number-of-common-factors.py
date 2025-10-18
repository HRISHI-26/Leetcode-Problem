class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        if a > b:
            for factor in range(1, b + 1):
                if a % factor == 0 and b % factor == 0:
                    count += 1
        elif b >= a:
            for factor in range(1, a + 1):
                if a % factor == 0 and b % factor == 0:
                    count += 1

        return count
