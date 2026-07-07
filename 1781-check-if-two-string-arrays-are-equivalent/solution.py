class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1=""
        str2=""
        for word in word1:
            str1+=word
        for word in word2:
            str2+=word
        return str1==str2        
