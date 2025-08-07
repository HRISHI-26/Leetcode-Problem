class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums_even = [x for x in nums if x % 2 == 0]
        nums_odd = [x for x in nums if x % 2 != 0]
        return nums_even + nums_odd