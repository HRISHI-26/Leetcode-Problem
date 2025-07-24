class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for _ in nums:
            count[_] = count.get(_, 0) + 1
            if count[_] > 1:
                return True
        return False
