class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            print(stone_1, stone_2)
            if stone_1 - stone_2 < 0:
                heapq.heappush(stones, stone_1 - stone_2)
        if not stones:
            return 0
        return abs(heapq.heappop(stones))

