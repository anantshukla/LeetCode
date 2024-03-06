class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist, res = [], []
        for x, y in points:
            dist.append(((x ** 2) + (y ** 2), x, y))
        
        heapq.heapify(dist)
        
        for _ in range(k):
            _, x, y = heapq.heappop(dist)
            res.append((x,  y))
        return res