class Solution:
    def isValid(self, s: str) -> bool:
        key_map = {"(":")", "[":"]", "{":"}"}
        stack = []
        for i in s:
            if i in key_map:
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if i != key_map[top]:
                    return False
        return not stack