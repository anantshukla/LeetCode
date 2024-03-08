class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMax = 0
        i = j = 0
        while j < len(prices):
            if prices[j] - prices[i] < 0:
                i = j
                continue
            curMax = max(curMax, prices[j] - prices[i])
            j += 1
        return curMax