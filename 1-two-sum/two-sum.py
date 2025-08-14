class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using Hash Map (dictionary)
        prev_map = {}

        for i, num in enumerate(nums):
            if target - num in prev_map:
                return [i, prev_map[target-num]]
            prev_map[num] = i
        
        return None