class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # In order to do it in O(1) memory complexity, we can do 2 passes of n**2 and 2 passes of n:
        # i. Visit all rows and mark 1st column as 0
        # ii. Visit all values and set 0 in row/column
        # iii. Visit first column then first row if value at 0th index is 0

        numRows, numCols = len(matrix), len(matrix[0])
        isFirstRowZero = False

        for i in range(numRows):
            for j in range(numCols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        isFirstRowZero = True
                        continue
                    matrix[i][0] = 0

        # If the value at 0th index is 0, set all vals in row/column = 0
        for i in range(1, numRows):
            for j in range(1, numCols):    
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(numRows):
                matrix[i][0] = 0
        
        if isFirstRowZero:
            for j in range(numCols):
                    matrix[0][j] = 0
