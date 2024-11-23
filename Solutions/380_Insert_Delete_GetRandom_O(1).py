class RandomizedSet:

    # Sep 23, 2024
    def __init__(self):
        self.dic = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False

        self.arr.append(val)
        self.dic[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False

        index = self.dic[val]
        last = self.arr[-1]
        self.arr[index] = last
        self.arr.pop()
        self.dic[last] = index
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        return choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()