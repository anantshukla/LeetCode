class Solution:
    # Greedy
    def canJump(self, nums: List[int]) -> bool:
        goalPtr = len(nums) - 1
        currPtr = goalPtr - 1
        for currPtr in range(len(nums) - 1, -1, -1):
            if nums[currPtr] >= goalPtr - currPtr:
                goalPtr = currPtr
        
        return goalPtr == 0