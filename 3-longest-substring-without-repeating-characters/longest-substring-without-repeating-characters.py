class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen, currSet = 0, set()
        while r < len(s):
            while s[r] in currSet:
                currSet.remove(s[l])
                l += 1
            
            currSet.add(s[r])
            r += 1
            maxLen = max(maxLen, len(currSet))
        return maxLen

        