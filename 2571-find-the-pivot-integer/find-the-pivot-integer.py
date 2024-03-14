class Solution:
    def pivotInteger(self, n: int) -> int:
        sumArray = [0] * n
        currSum = 0
        for i in range(n):
            currSum += i + 1
            sumArray[i] = currSum
        currSum = 0
        for i in range(n - 1, -1, -1):
            currSum += i + 1
            sumArray[i] -= currSum
        
        for idx, val in enumerate(sumArray):
            if val == 0:
                return idx + 1
        return -1

        