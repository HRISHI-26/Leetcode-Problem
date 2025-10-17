class Solution:
    def isValid(self, s: str) -> bool:
        symbol_table = {"(":")", "[":"]", "{":"}"}
        stack = []

        for symbol in s:
            if symbol in symbol_table:
                stack.append(symbol)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if symbol != symbol_table[top]:
                    return False
        return not stack