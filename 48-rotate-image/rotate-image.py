class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                top_left = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i] # Top left gets bottom left
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]   # bottom left gets bottom right
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]   # bottom right gets top right
                matrix[j][n-i-1] = top_left   # top right gets top left