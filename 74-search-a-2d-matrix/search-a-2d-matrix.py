class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        nRows, nCols = len(matrix), len(matrix[0])
        l, r = 0, nRows * nCols - 1
        while l <= r:
            mid = (l + r) // 2
            print(nRows, nCols, '-->', mid, mid // nCols, mid % nCols)
            if matrix[mid // nCols][mid % nCols] == target:
                return True
            elif matrix[mid // nCols][mid % nCols] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False