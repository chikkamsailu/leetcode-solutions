class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        j = n - 1
        for i in range(n):
            # Add the primary diagonal element
            s += mat[i][i]
            # Add the secondary diagonal element, but avoid double-counting the center element
            if i != j:
                s += mat[i][j]
            # Move j to the left for the next iteration (secondary diagonal)
            j -= 1
        return s


        
