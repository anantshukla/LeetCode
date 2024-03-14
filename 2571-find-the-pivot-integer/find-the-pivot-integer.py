class Solution:
    def pivotInteger(self, n: int) -> int:
        def sumOfnNums(n):
            return (n * (n + 1)) / 2

        totalSum = sumOfnNums(n)
        
        for i in range(1, n + 1):
            left = sumOfnNums(i)
            right = totalSum - sumOfnNums(i) + i
            if left == right:
                return i
        return -1

        # sumArray = [0] * n
        # currSum = 0
        # for i in range(n):
        #     currSum += i + 1
        #     sumArray[i] = currSum
        # currSum = 0
        # for i in range(n - 1, -1, -1):
        #     currSum += i + 1
        #     sumArray[i] -= currSum
        
        # for idx, val in enumerate(sumArray):
        #     if val == 0:
        #         return idx + 1
        # return -1

        