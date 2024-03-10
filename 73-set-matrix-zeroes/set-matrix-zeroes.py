class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # In order to do it in O(1) memory complexity, we can do three passes:
        # i. Visit all rows and mark 1st column as 0
        # ii. Visit all rows and set 0 in column
        # iii. Visit all columns and set 0 in row

        numRows, numCols = len(matrix), len(matrix[0])
        isFirstRowZero = False

        for i in range(numRows):
            for j in range(numCols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        isFirstRowZero = True
                    else:
                        matrix[i][0] = 0 

        # Scan the first row values and if the value is 0, set all rows with that column as 0
        for j in range(1, numCols):
            if matrix[0][j] == 0:
                for i in range(1, numRows):
                    matrix[i][j] = 0

        # Scan the first column and if the value is 0, set all rows with that row as 0
        for i in range(1, numRows):
            for j in range(1, numCols):    
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(1, numRows):
                matrix[i][0] = 0

        if isFirstRowZero:
            for j in range(numCols):
                    matrix[0][j] = 0
