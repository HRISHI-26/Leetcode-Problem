class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maximum = 0
        for char in s:
            if char == "(":
                count += 1
                if count > maximum:
                    maximum = count
            elif char ==")":
                count -= 1
        return maximum