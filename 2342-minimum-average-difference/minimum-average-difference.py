class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n, total_sum = len(nums), sum(nums)
        forward_sum, min_idx, min_diff = 0, 0, float('inf')

        for i, val in enumerate(nums):
            forward_sum += val

            l_avg = forward_sum // (i + 1)
            if n - i - 1 != 0:
                r_avg = (total_sum - forward_sum) // (n - i - 1)
            else:
                r_avg =  0

            if abs(r_avg - l_avg) < min_diff:
                min_diff = abs(r_avg - l_avg)
                min_idx = i
            
        return min_idx
        