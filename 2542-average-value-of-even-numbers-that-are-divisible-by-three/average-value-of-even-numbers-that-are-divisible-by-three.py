class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum_of_elements = 0
        count_of_elements = 0
        average = 0

        for number in nums:
            if number % 2 == 0 and number % 3 == 0:
                count_of_elements += 1
                sum_of_elements += number

        if count_of_elements != 0:
            average = sum_of_elements / count_of_elements
            return int(average)

        return 0
