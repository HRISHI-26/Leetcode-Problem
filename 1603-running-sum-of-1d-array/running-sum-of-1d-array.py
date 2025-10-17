class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for _ in nums:
            total += _
            result.append(total)
        
        return result