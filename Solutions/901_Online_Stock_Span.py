class StockSpanner:
    # A good example to use the Monotonic Decreasing Stack to solve this problem.
    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            # The stack is always decreasing order
            res += self.stack.pop()[1]
        self.stack.append((price, res))
        return self.stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)