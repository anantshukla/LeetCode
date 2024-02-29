class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount, numsSet = 0, set(nums)

        for num in numsSet:
            # If a 1 + num is present in the hash set, then continue
            if num + 1 in numsSet:
                continue
            # Find the lowest subsequence value
            curr = 1
            while num - curr in numsSet:
                curr += 1
            maxCount = max(curr, maxCount)
        return maxCount