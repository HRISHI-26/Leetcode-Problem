class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        count = 0
        maximum = 0

        for symbol in s:
            
            if symbol == "(" or symbol == ")":
                stack.append(symbol)
                
                if symbol == "(":
                    count += 1
                    if count > maximum:
                        maximum = count
                elif symbol == ")":
                    count -= 1
        return maximum