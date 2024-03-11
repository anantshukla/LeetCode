class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax, n = 0, len(prices)
        l = r = 0
        while r < n:
            currMax = max(currMax, prices[r] - prices[l])
            if prices[r] - prices[l] < 0:
                l = r
            r += 1
        return currMax
            
