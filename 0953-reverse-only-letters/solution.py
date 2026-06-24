class Solution:
    def reverseOnlyLetters(self, s):
        letters = [c for c in s if c.isalpha()]
        result = ""

        for c in s:
            if c.isalpha():
                result += letters.pop()
            else:
                result += c

        return result
