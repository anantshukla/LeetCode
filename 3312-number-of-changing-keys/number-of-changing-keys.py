class Solution:
    def countKeyChanges(self, s: str) -> int:
        res = 0
        lastChar = s[0].lower()
        for c in s[1:]:
            if lastChar != c.lower():
                lastChar = c.lower()
                res += 1        
        return res
        