class Solution:
    def myAtoi(self, s: str) -> int:
        # Constants for 32-bit signed integer range
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # Step 1: Trim leading whitespace
        s = s.lstrip()

        if not s:  # If string is empty after trimming
            return 0

        # Step 2: Determine the sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        # Step 3: Read digits and build the integer
        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        # Apply sign to the result
        result *= sign

        # Step 4: Clamp the result to the 32-bit signed integer range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
