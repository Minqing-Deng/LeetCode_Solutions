class MinStack:

    def __init__(self):
        self.os = []  # original stack
        self.ms = []  # aother stack that store the minimum that correspoding to each element

    def push(self, val: int) -> None:
        self.os.append(val)
        if not self.ms:
            self.ms.append(val)
        else:
            self.ms.append(min(val, self.ms[-1]))

    def pop(self) -> None:
        self.os.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.os[-1]

    def getMin(self) -> int:
        return self.ms[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()