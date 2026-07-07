class Solution:
    def firstUniqChar(self, s):
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
