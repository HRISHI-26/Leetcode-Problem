class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sumSingleDigit = 0
        sumMultiDigit = 0

        for num in nums:
            if num < 10:
                sumSingleDigit += num
            else:
                sumMultiDigit += num
        return sumSingleDigit != sumMultiDigit