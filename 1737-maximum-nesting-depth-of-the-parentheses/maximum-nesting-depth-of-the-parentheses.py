class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        maximum = 0
        for symbol in s:
            if symbol == "(" or symbol == ")":
                if symbol == "(":
                    counter += 1
                    maximum = max(maximum, counter)
                elif symbol == ")":
                    counter -= 1
        
        return maximum
