from collections import deque

class MyCircularDeque:

    def __init__(self, k):
        self.d = deque()
        self.k = k

    def insertFront(self, value):
        if len(self.d) == self.k:
            return False
        self.d.appendleft(value)
        return True

    def insertLast(self, value):
        if len(self.d) == self.k:
            return False
        self.d.append(value)
        return True

    def deleteFront(self):
        if not self.d:
            return False
        self.d.popleft()
        return True

    def deleteLast(self):
        if not self.d:
            return False
        self.d.pop()
        return True

    def getFront(self):
        return self.d[0] if self.d else -1

    def getRear(self):
        return self.d[-1] if self.d else -1

    def isEmpty(self):
        return len(self.d) == 0

    def isFull(self):
        return len(self.d) == self.k
        


