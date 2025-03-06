from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for a in asteroids:
            if not stack:
                stack.append(a)
            elif stack[-1] < 0 and a < 0:
                stack.append(a)
            elif stack[-1] > 0 and a > 0:
                stack.append(a)
            elif stack[-1] < 0 and a > 0:
                stack.append(a)
            else:  # stack[-1] > 0 and a < 0
                while stack and stack[-1] > 0 and stack[-1] < -a:
                    stack.pop()
                if stack and stack[-1] > 0 and stack[-1] == -a:
                    stack.pop()
                    continue
                elif stack and stack[-1] > 0 and stack[-1] > -a:
                    continue
                stack.append(a)

        return stack