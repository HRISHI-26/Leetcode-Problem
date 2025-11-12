class Solution:
    def toLowerCase(self, s: str) -> str:
        ascii_val = 0
        new_string = []
        string = list(s)
        for char in string:
            if ord(char) in range(65, 91):
                ascii_val = ord(char) + 32
                new_string.append(chr(ascii_val))
            else:
                new_string.append(char)

        new_string = "".join(new_string)
        return new_string
