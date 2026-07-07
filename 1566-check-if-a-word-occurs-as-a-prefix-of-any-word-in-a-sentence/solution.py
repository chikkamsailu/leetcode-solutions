class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        list1=sentence.split()
        l=len(searchWord)
        for i in range(len(list1)):
            name1=str(list1[i])
            if len(list1[i])>=len(searchWord) and name1[:l]==searchWord:
                return i+1
        return -1

        
        
