from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()

                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                elif token == '/':
                    # we use int() for truncation towards 0
                    stack.append(int(b / a))

        return stack.pop()