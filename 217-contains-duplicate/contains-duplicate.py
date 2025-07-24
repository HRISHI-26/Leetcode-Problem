class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = sorted(nums)
        if len(num) > 1:
            for _ in range(len(num)-1):
                if num[_] == num[_+1]:
                    return True
            return False
        else:
            return False
