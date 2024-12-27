class Solution:
    def fib(self, n: int) -> int:

        # Brute Force DFS solution:
        if n <= 1:
            return n

        return self.fib(n - 2) + self.fib(n - 1)

        # Cache DFS solution:
        if n <= 1:
            return n
        cache = [-1] * (n + 1)
        cache[0] = 0
        cache[1] = 1

        def helper(n):
            if cache[n] != -1:
                return cache[n]

            cache[n] = helper(n - 2) + helper(n - 1)

            return cache[n]

        return helper(n)

        # True DP solution:
        if n <= 1:
            return n

        preTwo = 0
        preOne = 1

        i = 2
        while i <= n:
            temp = preTwo + preOne
            preTwo = preOne
            preOne = temp
            i += 1
        return preOne