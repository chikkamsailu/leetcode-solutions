class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = int(num ** 0.5)
        if root * root == num:
            return True
        else:
            return False
