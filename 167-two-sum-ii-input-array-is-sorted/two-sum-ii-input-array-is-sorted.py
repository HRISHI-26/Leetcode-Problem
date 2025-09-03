class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1

        while left < right:
            sum_numbers = numbers[left] + numbers[right]

            if sum_numbers < target:
                left += 1
            elif sum_numbers > target:
                right -= 1
            else:
                return [left+1, right+1]