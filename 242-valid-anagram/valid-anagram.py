class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hMapS, hMapT = {}, {}
        for cs, ct in zip(s, t):
            if cs in hMapS:
                hMapS[cs] += 1
            else:
                hMapS[cs] = 1
            
            if ct in hMapT:
                hMapT[ct] += 1
            else:
                hMapT[ct] = 1

        return hMapS == hMapT