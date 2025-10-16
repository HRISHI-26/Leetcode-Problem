class Solution:
    def isPalindrome(self, x: int) -> bool:
        isPal = True
        x = str(x)
        for index in range(len(x) // 2):
            if x[index] != x[len(x) - index - 1]:
                return False

        return isPal
