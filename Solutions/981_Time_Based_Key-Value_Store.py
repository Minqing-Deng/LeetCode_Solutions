class TimeMap:

    def __init__(self):
        self.hashMap = {} # key: ([timestamp], [value])

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = ([timestamp], [value])
        else:
            self.hashMap[key][0].append(timestamp)
            self.hashMap[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""
        elif timestamp < self.hashMap[key][0][0]:
            return ""
        elif timestamp >= self.hashMap[key][0][-1]:
            return self.hashMap[key][1][-1]
        else:
            l = 0
            r = len(self.hashMap[key][0]) - 1
            res = self.hashMap[key][1][0]
            while l <= r:
                m = (l + r) // 2
                if self.hashMap[key][0][m] <= timestamp:
                    res = self.hashMap[key][1][m]
                    l = m + 1
                elif timestamp < self.hashMap[key][0][m]:
                    r = m - 1
            return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)