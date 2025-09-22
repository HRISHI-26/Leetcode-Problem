class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return list(set(range(1, len(nums) + 1)) - set(nums))