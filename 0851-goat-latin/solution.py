class Solution:
    def toGoatLatin(self, sentence):
        vowels = "aeiouAEIOU"
        words = sentence.split()
        result = []

        for i in range(len(words)):
            word = words[i]

            if word[0] in vowels:
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"

            word += "a" * (i + 1)
            result.append(word)

        return " ".join(result)
