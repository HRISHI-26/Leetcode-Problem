class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.split(" ")
        result = []
        for word in strings:
            result.append(word[::-1])

        result = " ".join(result)
        return result
