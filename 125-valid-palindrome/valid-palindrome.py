class Solution:
    def isPalindrome(self, s: str) -> bool:
        removed = ""
        for i in s:
            if i.isalnum():
                removed += i
        ns = removed.lower()
        if ns == ns[::-1]:
            return True
        return False
        