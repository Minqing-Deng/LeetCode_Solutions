from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.freq = {}  # Dictionary to track frequency of elements
        self.group = defaultdict(list)  # Dictionary of stacks grouped by frequency
        self.max_freq = 0  # Track the current maximum frequency

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]
        self.group[f].append(val)  # Push to the corresponding frequency stack
        self.max_freq = max(self.max_freq, f)  # Update max frequency

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()  # Pop the most frequent element
        self.freq[val] -= 1  # Decrease its frequency count
        if not self.group[self.max_freq]:  # If the stack is empty, reduce max_freq
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()