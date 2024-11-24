from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ones, twos = 0, 0
        for num in nums:
            # The basic idea is that ones will hold bits that appear exactly once so far,
            # and twos will hold bits that appear exactly twice.
            # Whenever a bit has appeared three times, both ones and twos will drop that bit.
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones