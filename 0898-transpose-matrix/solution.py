class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(matrix[0])):  # Loop through columns
            row = []
            for j in range(len(matrix)):  # Loop through rows
                row.append(matrix[j][i])  # Add the element to the new row
            result.append(row)  # Append the row to the result matrix
        return result

        
