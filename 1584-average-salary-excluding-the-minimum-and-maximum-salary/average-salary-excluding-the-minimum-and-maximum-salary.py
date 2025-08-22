class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        list_sum = 0
        for i, num in enumerate(salary[1:-1]):
            list_sum += num
        n = len(salary) - 2
        average = list_sum / n
        return average