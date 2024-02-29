class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hMapS, hMapT = {}, {}
        for i in range(len(s)):
            cs, ct = s[i], t[i]
            hMapS[cs] = 1 + hMapS.get(cs, 0)
            hMapT[ct] = 1 + hMapT.get(ct, 0)
        return hMapS == hMapT