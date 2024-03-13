class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        onePrev, twoPrev = 1, 1
        curr = 0
        for i in range(2, n + 1):
            curr = onePrev + twoPrev
            twoPrev = onePrev
            onePrev = curr
        return curr

        # if n == 1:
        #     return 1
        # arr = [1] * (n + 1)
        # for i in range(2, n + 1):
        #     arr[i] = arr[i - 1] + arr[i - 2]
        # return arr[n]

        # def numOfWays(remaining):
        #     if remaining == 1 or remaining == 0:
        #         return 1
        #     else:
        #         return numOfWays(remaining - 1) + numOfWays(remaining - 2)
        # return numOfWays(n)