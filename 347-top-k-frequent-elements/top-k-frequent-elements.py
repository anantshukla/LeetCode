class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreqMap = {}
        for num in nums:
            numFreqMap[num] = 1 + numFreqMap.get(num, 0)

        heapList = [(-freq, num) for num, freq in numFreqMap.items()]
        heapq.heapify(heapList)
        res = []
        for _ in range(k):
            _, num = heapq.heappop(heapList)
            res.append(num)
        return res