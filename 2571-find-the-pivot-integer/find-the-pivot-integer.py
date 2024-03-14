class Solution:
    def pivotInteger(self, n: int) -> int:
        # Using Sum of Arithematic Progression
        def sumOfnNums(n):
            return (n * (n + 1)) / 2

        totalSum = sumOfnNums(n)
        
        for i in range(1, n + 1):
            left = sumOfnNums(i)
            right = totalSum - sumOfnNums(i) + i
            if left == right:
                return i
        return -1

        