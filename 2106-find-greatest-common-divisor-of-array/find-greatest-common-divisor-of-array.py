class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min = 1001
        max = 0
        if len(nums) >= 1 and len(nums) <= 1000:
            for i in nums:
                if i < min:
                    min = i
                if i > max:
                    max = i
            
            for i in range(1, min+1):
                if min % i == 0 and max % i == 0:
                    gcd = i
            return gcd

