class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_v, n = max(nums), len(nums)
        l = 0
        max_count = 0
        res = 0

        for r in range(n):
            if nums[r] == max_v:
                max_count += 1
            
            while max_count == k:
                res = res + n - r
                if nums[l] == max_v:
                    max_count -= 1
                l += 1
        return res
        