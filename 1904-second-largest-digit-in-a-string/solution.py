class Solution:
    def secondHighest(self, s: str) -> int:
        second=-1
        first=None
        num=None
        for i in s:
            if i.isdigit():
                num=int(i)
            if first==None:
                first=num
            elif num<first:
                second=max(second,num)
            elif num>first:
                temp=first
                first=num
                second=temp
        return second
        
