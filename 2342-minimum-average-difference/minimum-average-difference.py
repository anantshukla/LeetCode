class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = sum(nums)

        ansIdx, leftSum = 0, 0
        minDiff = 10 ** 6
        
        for i in range(n):
            leftSum += nums[i]
            lAvg = math.floor(leftSum/(i+1))
            rAvg = math.floor(totalSum - leftSum) // (n - i - 1) if (n - i - 1) !=0 else 0

            currDiff = int(abs(rAvg - lAvg))

            if currDiff < minDiff:
                minDiff = currDiff
                ansIdx = i
        
        return ansIdx

        