class Solution:
    def partitionString(self, s: str) -> int:
        setChars, numPart = set(), 1
        for c in s:
            if c in setChars:
                setChars.clear()
                numPart += 1
            setChars.add(c)
        return numPart