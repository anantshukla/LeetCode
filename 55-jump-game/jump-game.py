class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        canReachPtr = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= canReachPtr:
                canReachPtr = i
        
        return canReachPtr == 0