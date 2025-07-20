class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum = []
        for i in range(len(nums)):
            if i == 0:
                runningsum.append(nums[i])
            else:
                nums[i] += nums[i-1]
                runningsum.append(nums[i])
        return runningsum