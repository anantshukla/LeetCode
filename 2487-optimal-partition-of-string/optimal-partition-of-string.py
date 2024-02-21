class Solution:
    def partitionString(self, s: str) -> int:
        num_partitions = 1
        setV = set()
        for char in s:
            if char in setV:
                num_partitions += 1
                setV.clear()
            setV.add(char)
        return num_partitions


        