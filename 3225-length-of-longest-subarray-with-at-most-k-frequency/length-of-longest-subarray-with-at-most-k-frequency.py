class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l, r, res = 0, 0, 0
        window = defaultdict(int)
        while r < len(nums):
            while window[nums[r]] >= k:
                window[nums[l]] -= 1
                l += 1
            window[nums[r]] += 1
            res = max(res, r - l + 1)
            r += 1
        return res
