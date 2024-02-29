class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount, numsSet = 0, set(nums)

        for num in numsSet:
            # If a number smaller than num is present, then continue
            if num - 1 in numsSet:
                continue
            curr = 1
            while num + curr in numsSet:
                curr += 1
            maxCount = max(maxCount, curr)
        return maxCount
