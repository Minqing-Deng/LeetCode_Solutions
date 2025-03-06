from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == "+":
                v1 = stack.pop()
                v2 = stack[-1]
                stack.append(v1)
                stack.append(v1 + v2)
            elif o == "D":
                stack.append(stack[-1] * 2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))

        return sum(stack)