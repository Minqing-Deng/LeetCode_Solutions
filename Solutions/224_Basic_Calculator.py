class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        cur = 0
        res = 0
        sign = 1

        for e in s:

            if e.isdigit():
                cur = cur * 10 + int(e)

            elif e in ["+", "-"]:
                res += sign * cur
                if e == "+":
                    sign = 1
                else:
                    sign = -1
                cur = 0

            elif e == "(":
                stack.append(res)
                stack.append(sign)

                res = 0
                sign = 1

            elif e == ")":
                res += sign * cur
                res *= stack.pop()
                res += stack.pop()
                cur = 0

        res += sign * cur