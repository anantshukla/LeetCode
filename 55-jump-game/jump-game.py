class Solution:
    # Greedy
    def canJump(self, nums: List[int]) -> bool:
        goalPtr = len(nums) - 1
        currPtr = goalPtr - 1
        while currPtr >=0:
            if nums[currPtr] >= goalPtr - currPtr:
                goalPtr = currPtr
            currPtr -= 1
        
        return (currPtr == -1 and goalPtr == 0)