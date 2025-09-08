class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1
        str_list = list(str(num))
        int_list = list(map(int, str_list))
        return int_list