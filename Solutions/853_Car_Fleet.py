from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        # use Stack
        stack = []
        stack.append((target - pairs[0][0]) / pairs[0][1])
        for i in range(1, len(pairs)):
            if (target - pairs[i][0]) / pairs[i][1] <= stack[-1]:
                continue
            else:
                stack.append((target - pairs[i][0]) / pairs[i][1])

        return len(stack)


        # # not use Stack
        # res = 1
        # i = 0

        # while i < len(pairs):
        #     j = i + 1
        #     while j < len(pairs) and (target - pairs[j][0]) / pairs[j][1] <= (target - pairs[i][0]) / pairs[i][1]:
        #         j += 1
        #     i = j
        #     if i < len(pairs):
        #         res += 1

        # return res