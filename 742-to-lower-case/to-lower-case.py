class Solution:
    def toLowerCase(self, s: str) -> str:
        lower = ""
        for char in s:
            if ord(char) in range(65, 91):
                value = chr(ord(char) + 32)
                lower += value
                continue
            lower += char
            
        
        return lower
