class Solution:
    def climbStairs(self, n: int) -> int:

        # # Brute Force DFS solution:
        # if n <= 2:
        #     return n

        # return self.climbStairs(n-1) + self.climbStairs(n-2)


        # # Cache DFS solution:
        # if n <= 2:
        #     return n

        # # [0, 1, 2, ..., n], index 0 is just a dummy index
        # cache = [-1] * (n+1)
        # cache[1] = 1
        # cache[2] = 2

        # def helper(n):
        #     if cache[n] != -1:
        #         return cache[n]

        #     cache[n] = helper(n-1) + helper(n-2)

        #     return cache[n]

        # return helper(n)


        # True DP solution:
        if n <= 2:
            return n

        preTwo = 1
        preOne = 2

        i = 3
        while i <= n:
            temp = preTwo + preOne
            preTwo = preOne
            preOne = temp
            i += 1
        return preOne