class Solution:
    def pivotInteger(self, n: int) -> int:
        sumArray = [0] * n
        currSum = 0
        for i in range(n):
            currSum += i + 1
            sumArray[i] = currSum
        print(sumArray)
        currSum = 0
        for i in range(n - 1, -1, -1):
            currSum += i + 1
            sumArray[i] -= currSum

        print(sumArray)
        
        for idx, val in enumerate(sumArray):
            if val == 0:
                return idx + 1
        print(sumArray)
        return -1

        