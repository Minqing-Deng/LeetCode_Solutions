from collections import defaultdict
from typing import List


class DetectSquares:

    def __init__(self):
        self.pointCounts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pointCounts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in list(self.pointCounts.keys()):
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            res += self.pointCounts[(x, py)] * self.pointCounts[(px, y)] * self.pointCounts[(x, y)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)