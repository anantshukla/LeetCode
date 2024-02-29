class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount, numsSet = 0, set(nums)

        for num in numsSet:
            # We can ignore all values where num + 1 exist in the hash set
            # Because we are searching for the upper bound of this subsequence
            if num + 1 in numsSet:
                continue
            # We are at upper bound of this subsequence
            # Now find the lower bound of the current subsequence
            curr = 1
            while num - curr in numsSet:
                curr += 1
            maxCount = max(curr, maxCount)
        return maxCount