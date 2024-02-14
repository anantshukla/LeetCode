class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        strLen = len(s)
        dp = [False] * (strLen + 1)
        dp[strLen] = True

        for i in range (strLen - 1, -1, -1):
            for word in wordDict:
                if len(word) <= strLen - i and word == s[i: i + len(word)]:
                    dp[i] = dp[i + len(word)]
                    
                    if dp[i] == True:
                        break
        
        return dp[0]
                    
        