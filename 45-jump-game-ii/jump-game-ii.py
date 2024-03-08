class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        ans = 0
        while r < (len(nums) - 1):
            maxRight = 0
            for i in range(l, r + 1):
                maxRight = max(i + nums[i], maxRight)
            l = r + 1
            r = maxRight
            ans += 1
        return ans