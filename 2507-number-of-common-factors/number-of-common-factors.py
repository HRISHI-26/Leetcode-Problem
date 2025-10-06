class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        minimum = min(a, b)
        
        for num in range(1, minimum+1):
            if a % num == 0 and b % num == 0:
                count += 1
        
        return count
                