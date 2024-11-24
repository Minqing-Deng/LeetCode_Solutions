class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        # while left != right:
        while right - left >= 1:
            left = left >> 1
            right = right >> 1
            count += 1

        return left << count

        # # Time: O(n)
        # res = 0
        # for i in range(32):
        #     res += (1 << i)

        # for num in range(left, right+1):
        #     res = res & num

        # return res