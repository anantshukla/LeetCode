class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreqMap = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            numFreqMap[num] = 1 + numFreqMap.get(num, 0)
        
        for num, count in numFreqMap.items():
            buckets[count].append(num)
        res = []
        # O(n + n)
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # # O(n * k.log(n))
        # heapList = [(-freq, num) for num, freq in numFreqMap.items()]
        # heapq.heapify(heapList)
        # res = []
        # for _ in range(k):
        #     _, num = heapq.heappop(heapList)
        #     res.append(num)
        # return res