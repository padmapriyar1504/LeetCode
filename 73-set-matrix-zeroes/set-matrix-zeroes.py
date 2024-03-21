class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_positions = set()
        
        # Identify the positions of all zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_positions.add((i, j))
        
        # Set entire rows and columns to zeros based on zero positions
        for row, col in zero_positions:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
            for i in range(len(matrix)):
                matrix[i][col] = 0
          
        