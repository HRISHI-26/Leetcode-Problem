class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = salary[0]
        maximum = salary[0]
        for i in salary:
            if i <= minimum:
                minimum = i
            elif i >= maximum:
                maximum = i

        salary.remove(minimum)
        salary.remove(maximum)

        list_sum = 0
        for i in salary:
            list_sum += i
        n = len(salary)
        average = list_sum / n
        return average
