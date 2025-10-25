class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maximum = 0
        for char in s:
            if char == "(":
                depth += 1
                maximum = max(depth, maximum)
            elif char == ")":
                depth -= 1
        
        return maximum