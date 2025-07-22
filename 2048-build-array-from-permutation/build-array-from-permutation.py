class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        if len(nums) in range(1, 1001):
            ans = [nums[nums[i]] for i in range(len(nums))]
            return ans