class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        res1 = 0
        k = 0
        for c in num1[::-1]:
            digit = ord(c) - ord("0")
            res1 += digit * (10 ** k)
            k += 1

        res2 = 0
        k = 0
        for c in num2[::-1]:
            digit = ord(c) - ord("0")
            res2 += digit * (10 ** k)
            k += 1

        return str(res1 * res2)