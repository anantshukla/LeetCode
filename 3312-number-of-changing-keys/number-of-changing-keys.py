class Solution:
    def countKeyChanges(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(1, n):
            if s[i].lower() != s[i - 1].lower():
                res += 1        
        return res
        