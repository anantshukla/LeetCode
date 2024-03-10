class DetectSquares:
    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point
        for (x, y), count in self.pointsCount.items():
            # Checking if the iter point forms a diagonal with given point
            if x != px and abs(x - px) == abs(y - py) and (px, y) in self.pointsCount and (x, py) in self.pointsCount:
                ans += count * self.pointsCount[(px, y)] * self.pointsCount[(x, py)]
        return ans



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)