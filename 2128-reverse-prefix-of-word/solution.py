class Solution:
    def reversePrefix(self, word, ch):
        idx = word.find(ch)

        if idx == -1:
            return word

        return word[:idx + 1][::-1] + word[idx + 1:]
        
