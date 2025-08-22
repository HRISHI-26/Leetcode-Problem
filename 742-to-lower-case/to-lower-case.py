class Solution:
    def toLowerCase(self, s: str) -> str:
        ls = ""
        for i in s: 
            if ord(i) <= 90 and ord(i) >= 65: 
                c = ord(i)
                c += 32
                i = chr(c)
            ls += i
        return ls