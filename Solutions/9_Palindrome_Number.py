class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        count = 0
        while n > 0:
            n = n // 10
            count += 1
        # the count is the number of digit of x

        for i in range(1, (count // 2) + 1):

            if (x // (10 ** (i - 1))) % 10 != (x // (10 ** (count - i))) % 10:
                return False
        return True

        # x_str = str(x)
        # l = 0
        # r = len(x_str) - 1

        # while l < r:
        #     if x_str[l] != x_str[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True