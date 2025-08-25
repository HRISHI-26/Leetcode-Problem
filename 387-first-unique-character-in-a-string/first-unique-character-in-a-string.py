class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        else:
            for i in range(len(s)):
                if i != len(s)-1:
                    if s[i] != s[i+1] and s.count(s[i]) == 1:
                        return i
                        break
                elif s[i] != s[i-1] and s.count(s[i]) == 1:
                    return i
                    break
            return -1