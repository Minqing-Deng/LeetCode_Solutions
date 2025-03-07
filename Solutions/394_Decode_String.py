class Solution:
    def decodeString(self, s: str) -> str:

        # Using a stack to append all the characters into the stack
        # unless the closing bracket
        # when encounter the closing bracket
        # pop the stack and do the repeating work
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                subString = ""
                while stack[-1] != "[":
                    subString = stack.pop() + subString
                stack.pop()
                repeat = ""
                while stack and stack[-1].isdigit():
                    repeat = stack.pop() + repeat
                stack.append(int(repeat) * subString)

        return "".join(stack)