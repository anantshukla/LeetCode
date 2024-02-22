class Solution:
    def partitionString(self, s: str) -> int:
        setC = set()
        numPart = 1
        for c in s:
            if c in setC:
                setC.clear()
                numPart += 1
            setC.add(c)
        return numPart