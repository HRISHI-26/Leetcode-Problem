class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1] and nums[i] != "_":
                nums.remove(nums[i+1])
                nums.append("_")
                i -= 1
            i += 1
        k = 0
        for i in nums:
            if i != "_":
                k += 1
        return k