class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = 0, nums[0]
        for v in nums:
            if currSum < 0: currSum = 0
            currSum += v
            maxSum = max(maxSum, currSum)
        return maxSum
            
            


        