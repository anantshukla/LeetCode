class Solution:
    def partitionString(self, s: str) -> int:
        num_partitions = 1
        setV = set()
        for c in s:
            if c in setV:
                num_partitions += 1
                setV.clear()
            setV.add(c)
        return num_partitions


        