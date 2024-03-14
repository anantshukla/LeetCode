class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        last, lastToLast = 0, 0
        for i in range(n):
            temp = max(lastToLast + nums[i], last)
            lastToLast = last
            last = temp
        return last
        