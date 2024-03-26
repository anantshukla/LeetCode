class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        l = r = 0
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l = r
            currMax = max(currMax, prices[r] - prices[l])
            r += 1
        return currMax
