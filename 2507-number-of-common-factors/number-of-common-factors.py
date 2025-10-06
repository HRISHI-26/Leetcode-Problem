class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0

        if a > b:
            for num in range(1, b+1):
                if a % num == 0 and b % num == 0:
                    count += 1
        else:
            for num in range(1, a+1):
                if a % num == 0 and b % num == 0:
                    count += 1
        
        return count
                