class Solution:
    def trailingZeroes(self, n: int) -> int:

        count = 0
        # Iterate over powers of 5
        while n >= 5:
            n //= 5
            count += n
        return count