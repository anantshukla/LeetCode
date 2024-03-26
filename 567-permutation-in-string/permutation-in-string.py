class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        arr1, arr2 = [0] * 26, [0] * 26

        if len(s2) < windowSize:
            return False

        for i in range(windowSize):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1

        if arr1 == arr2:
            return True
        
        for r in range(windowSize, len(s2)):
            lIdxVal = ord(s2[r - windowSize]) - ord('a')
            rIdxVal = ord(s2[r]) - ord('a')
            arr2[lIdxVal] -= 1
            arr2[rIdxVal] += 1
            if arr1 == arr2:
                return True
        return False

        