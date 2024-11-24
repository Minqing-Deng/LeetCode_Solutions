from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        carry = 1
        res = []

        for digit in digits:
            temp = digit + carry
            res.append(temp % 10)
            carry = temp // 10

        if carry:
            res.append(carry)

        return res[::-1]