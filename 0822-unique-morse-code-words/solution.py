class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]

        s = set()

        for word in words:
            code = ""
            for ch in word:
                code += morse[ord(ch) - ord('a')]
            s.add(code)

        return len(s)
