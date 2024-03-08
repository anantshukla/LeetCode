class Solution:
    # Greedy - TC: O(n), SC: O(1)
    def canJump(self, nums: List[int]) -> bool:
        goalPtr = len(nums) - 1
        currPtr = goalPtr - 1
        for currPtr in range(len(nums) - 1, -1, -1):
            if nums[currPtr] >= goalPtr - currPtr:
                goalPtr = currPtr
        return goalPtr == 0
    
    # DP - TC: O(n^2), SC: O(n)
    # def canJump(self, nums: List[int]) -> bool:
    #     dp = [False] * len(nums)
    #     dp[0] = True # B'cuz we start at 0, so we know it is accessible
    #     for i in range(1, len(nums)):
    #         for j in range(i - 1, -1, -1):
    #             if nums[j] >= i - j and dp[j]:
    #                 dp[i] = True
    #                 break
    #     return dp[-1]