class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(2, n):
            cost[i] = min(cost[i - 2], cost[i - 1]) + cost[i]
        return min(cost[n - 1], cost[n - 2])


        # n = len(cost)
        # costArr = [0] * n
        # costArr[n-1] = cost[n-1]
        # costArr[n-2] = cost[n-2]
        # for i in range(n-3, -1, -1):
        #     costArr[i] = min(costArr[i + 1], costArr[i + 2]) + cost[i]
        # return min(costArr[0], costArr[1])