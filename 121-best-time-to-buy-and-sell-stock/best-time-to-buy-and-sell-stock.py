class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = l = r = 0
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l = r
                continue
            currMax = max(currMax, prices[r] - prices[l])
            r += 1
            
        return currMax
            
