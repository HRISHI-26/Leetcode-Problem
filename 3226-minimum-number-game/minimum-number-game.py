class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []

        while nums:
            temp = nums.pop(0)
            if nums:
                ans.append(nums.pop(0))
            ans.append(temp)

        return ans
