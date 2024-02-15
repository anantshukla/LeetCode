class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLArr = [0] * n
        maxRArr = [0] * n
        totalWater = 0

        for i in range(1, n):
            maxLArr[i] = max(height[i-1], maxLArr[i-1])
        for i in range(n - 2, -1, -1):
            maxRArr[i] = max(height[i+1], maxRArr[i+1])

        for i in range(n):
            waterTrapped = min(maxLArr[i], maxRArr[i])
            if waterTrapped > height[i]:
                totalWater += waterTrapped - height[i]
        
        return totalWater
