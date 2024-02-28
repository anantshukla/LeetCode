class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > interval[1]:
                result.append(interval)
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]
        result.append(newInterval)
        return result
