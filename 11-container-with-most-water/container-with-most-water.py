class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Area = min-height * distance between i, j
        maxCap = 0
        l, r = 0, len(height) - 1
        lMaxHeight, lPos = 0, 0
        while l < r:
            maxCap = max(maxCap, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxCap