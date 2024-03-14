class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # n = len(cost)
        # for i in range(2, n):
        #     cost[i] = min(cost[i - 2], cost[i - 1]) + cost[i]
        # return min(cost[n - 1], cost[n - 2])

        n = len(cost)
        for i in range(n - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])