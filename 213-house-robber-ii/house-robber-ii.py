class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxCostRobbed(nums):
            # prev2, prev1, n, ........
            prev2, prev1 = 0, 0
            for num in nums:
                temp = max(prev2 + num, prev1)
                prev2 = prev1
                prev1 = temp
            return prev1
        return max(maxCostRobbed([nums[0]]), maxCostRobbed(nums[1:]), maxCostRobbed(nums[:-1]))