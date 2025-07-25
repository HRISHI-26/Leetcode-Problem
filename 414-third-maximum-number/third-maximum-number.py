class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) in range(1, 3):
            return max(nums)
        else:
            for _ in range(2):
                max_value = max(nums)
                nums.remove(max_value)
            max_value = max(nums)
            return max_value
