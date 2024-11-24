class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in closeToOpen:  # c is close symblo
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False  # ), (]
            else:  # c is open symblo
                stack.append(c)

        return len(stack) == 0