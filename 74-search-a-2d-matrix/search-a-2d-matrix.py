class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        newArr = []
        for row in matrix:
            for element in row:
                newArr.append(element)
        l, r = 0, len(newArr) - 1
        while l<=r:
            mid = (l + r) // 2
            if newArr[mid] == target:
                return True
            elif newArr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False