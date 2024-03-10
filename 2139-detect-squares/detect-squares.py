class DetectSquares:
    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        ans = 0
        givenX, givenY = point
        for iterX, iterY in self.points:
            # Checking if the iter point forms a diagonal with given point
            if abs(iterX - givenX) != abs(iterY - givenY) or iterX == givenX or iterY == givenY:
                continue
            ans += self.pointsCount[(givenX, iterY)] * self.pointsCount[(iterX, givenY)]
        return ans



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)