class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        nums.sort()
        for index in range(len(nums)):
            if nums[index] == target:
                result.append(index)

        return result