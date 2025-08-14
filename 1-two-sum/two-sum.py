class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Bruteforce method
        for i, num1 in enumerate(nums[:-1]):
            for j, num2 in enumerate(nums[i+1:], start=i+1):
                if num1 + num2 == target:
                    return [i, j]