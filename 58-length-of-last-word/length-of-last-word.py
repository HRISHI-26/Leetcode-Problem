class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip(" ")
        if len(s) > 1:
            for _ in range(len(s[::-1])-1,-1,-1):
                if s[_] == ' ':
                    return len(s[_+1:])
        return len(s)

            