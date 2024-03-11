class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = l = r = 0
        while r < len(prices):
            currMax = max(currMax, prices[r] - prices[l])
            if prices[r] - prices[l] < 0:
                l = r
                r += 1
                continue
            r += 1
        return currMax
            
