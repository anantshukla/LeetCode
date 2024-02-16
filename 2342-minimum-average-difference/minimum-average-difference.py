class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = sum(nums)

        ansIdx, leftSum = 0, 0
        minDiff = float('inf')
        
        for i in range(n):
            leftSum += nums[i]
            lAvg = leftSum // (i+1)
            rAvg = (totalSum - leftSum) // (n - i - 1) if (n - i - 1) !=0 else 0

            currDiff = int(abs(rAvg - lAvg))

            if currDiff < minDiff:
                minDiff = currDiff
                ansIdx = i
        
        return ansIdx

        