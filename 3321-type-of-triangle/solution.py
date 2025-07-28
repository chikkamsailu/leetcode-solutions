class Solution:
    def triangleType(self, nums: list[int]) -> str:
        a, b, c = nums

        # Check if it can form a triangle
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
        
        # Check the type
        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"

